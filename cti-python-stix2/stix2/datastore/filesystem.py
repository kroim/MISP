"""
Python STIX 2.0 FileSystem Source/Sink

"""

import errno
import json
import os
import stat

import pytz
import six

from stix2.base import _STIXBase
from stix2.core import Bundle, parse
from stix2.datastore import DataSink, DataSource, DataStoreMixin
from stix2.datastore.filters import Filter, FilterSet, apply_common_filters
from stix2.utils import get_type_from_id, is_marking


def _timestamp2filename(timestamp):
    """
    Encapsulates a way to create unique filenames based on an object's
    "modified" property value.  This should not include an extension.

    :param timestamp: A timestamp, as a datetime.datetime object.
    """
    # Different times will only produce different file names if all timestamps
    # are in the same time zone!  So if timestamp is timezone-aware convert
    # to UTC just to be safe.  If naive, just use as-is.
    if timestamp.tzinfo is not None:
        timestamp = timestamp.astimezone(pytz.utc)

    return timestamp.strftime("%Y%m%d%H%M%S%f")


class AuthSet(object):
    """
    Represents either a whitelist or blacklist of values, where/what we
    must/must not search to find objects which match a query.  (Maybe "AuthSet"
    isn't the right name, but determining authorization is a typical context in
    which black/white lists are used.)

    The set may be empty.  For a whitelist, this means you mustn't search
    anywhere, which means the query was impossible to match, so you can skip
    searching altogether.  For a blacklist, this means nothing is excluded
    and you must search everywhere.
    """

    BLACK = 0
    WHITE = 1

    def __init__(self, allowed, prohibited):
        """
        Initialize this AuthSet from the given sets of allowed and/or
        prohibited values.  The type of set (black or white) is determined
        from the allowed and/or prohibited values given.

        :param allowed: A set of allowed values (or None if no allow filters
            were found in the query)
        :param prohibited: A set of prohibited values (not None)
        """
        if allowed is None:
            self.__values = prohibited
            self.__type = AuthSet.BLACK

        else:
            # There was at least one allow filter, so create a whitelist.  But
            # any matching prohibited values create a combination of conditions
            # which can never match.  So exclude those.
            self.__values = allowed - prohibited
            self.__type = AuthSet.WHITE

    @property
    def values(self):
        """
        Get the values in this white/blacklist, as a set.
        """
        return self.__values

    @property
    def auth_type(self):
        """
        Get the type of set: AuthSet.WHITE or AuthSet.BLACK.
        """
        return self.__type

    def __repr__(self):
        return "{}list: {}".format(
            "white" if self.auth_type == AuthSet.WHITE else "black",
            self.values
        )


# A fixed, reusable AuthSet which accepts anything.  It came in handy.
_AUTHSET_ANY = AuthSet(None, set())


def _update_allow(allow_set, value):
    """
    Updates the given set of "allow" values.  The first time an update to the
    set occurs, the value(s) are added.  Thereafter, since all filters are
    implicitly AND'd, the given values are intersected with the existing allow
    set, which may remove values.  At the end, it may even wind up empty.

    :param allow_set: The allow set, or None
    :param value: The value(s) to add (single value, or iterable of values)
    :return: The updated allow set (not None)
    """
    adding_seq = hasattr(value, "__iter__") and \
        not isinstance(value, six.string_types)

    if allow_set is None:
        allow_set = set()
        if adding_seq:
            allow_set.update(value)
        else:
            allow_set.add(value)

    else:
        # strangely, the "&=" operator requires a set on the RHS
        # whereas the method allows any iterable.
        if adding_seq:
            allow_set.intersection_update(value)
        else:
            allow_set.intersection_update({value})

    return allow_set


def _find_search_optimizations(filters):
    """
    Searches through all the filters, and creates white/blacklists of types and
    IDs, which can be used to optimize the filesystem search.

    :param filters: An iterable of filter objects representing a query
    :return: A 2-tuple of AuthSet objects: the first is for object types, and
        the second is for object IDs.
    """

    # The basic approach to this is to determine what is allowed and
    # prohibited, independently, and then combine them to create the final
    # white/blacklists.

    allowed_types = allowed_ids = None
    prohibited_types = set()
    prohibited_ids = set()

    for filter_ in filters:
        if filter_.property == "type":
            if filter_.op in ("=", "in"):
                allowed_types = _update_allow(allowed_types, filter_.value)
            elif filter_.op == "!=":
                prohibited_types.add(filter_.value)

        elif filter_.property == "id":
            if filter_.op == "=":
                # An "allow" ID filter implies a type filter too, since IDs
                # contain types within them.
                allowed_ids = _update_allow(allowed_ids, filter_.value)
                allowed_types = _update_allow(allowed_types,
                                              get_type_from_id(filter_.value))
            elif filter_.op == "!=":
                prohibited_ids.add(filter_.value)
            elif filter_.op == "in":
                allowed_ids = _update_allow(allowed_ids, filter_.value)
                allowed_types = _update_allow(allowed_types, (
                    get_type_from_id(id_) for id_ in filter_.value
                ))

    opt_types = AuthSet(allowed_types, prohibited_types)
    opt_ids = AuthSet(allowed_ids, prohibited_ids)

    # If we have both type and ID whitelists, perform a type-based intersection
    # on them, to further optimize.  (Some of the cross-property constraints
    # occur above; this is essentially a second pass which operates on the
    # final whitelists, which among other things, incorporates any of the
    # prohibitions found above.)
    if opt_types.auth_type == AuthSet.WHITE and \
            opt_ids.auth_type == AuthSet.WHITE:

        opt_types.values.intersection_update(
            get_type_from_id(id_) for id_ in opt_ids.values
        )

        opt_ids.values.intersection_update(
            id_ for id_ in opt_ids.values
            if get_type_from_id(id_) in opt_types.values
        )

    return opt_types, opt_ids


def _get_matching_dir_entries(parent_dir, auth_set, st_mode_test=None, ext=""):
    """
    Search a directory (non-recursively), and find entries which match the
    given criteria.

    :param parent_dir: The directory to search
    :param auth_set: an AuthSet instance, which represents a black/whitelist
        filter on filenames
    :param st_mode_test: A callable allowing filtering based on the type of
        directory entry.  E.g. just get directories, or just get files.  It
        will be passed the st_mode field of a stat() structure and should
        return True to include the file, or False to exclude it.  Easy thing to
        do is pass one of the stat module functions, e.g. stat.S_ISREG.  If
        None, don't filter based on entry type.
    :param ext: Determines how names from auth_set match up to directory
        entries, and allows filtering by extension.  The extension is added
        to auth_set values to obtain directory entries; it is removed from
        directory entries to obtain auth_set values.  In this way, auth_set
        may be treated as having only "basenames" of the entries.  Only entries
        having the given extension will be included in the results.  If not
        empty, the extension MUST include a leading ".".  The default is the
        empty string, which will result in direct comparisons, and no
        extension-based filtering.
    :return: A list of directory entries matching the criteria.  These will not
        have any path info included; they will just be bare names.
    :raises OSError: If there are errors accessing directory contents or
        stat()'ing files
    """

    results = []
    if auth_set.auth_type == AuthSet.WHITE:
        for value in auth_set.values:
            filename = value + ext
            try:
                if st_mode_test:
                    s = os.stat(os.path.join(parent_dir, filename))
                    type_pass = st_mode_test(s.st_mode)
                else:
                    type_pass = True

                if type_pass:
                    results.append(filename)
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise
                # else, file-not-found is ok, just skip

    else:  # auth_set is a blacklist
        for entry in os.listdir(parent_dir):
            if ext:
                auth_name, this_ext = os.path.splitext(entry)
                if this_ext != ext:
                    continue
            else:
                auth_name = entry

            if auth_name in auth_set.values:
                continue

            try:
                if st_mode_test:
                    s = os.stat(os.path.join(parent_dir, entry))
                    type_pass = st_mode_test(s.st_mode)
                else:
                    type_pass = True

                if type_pass:
                    results.append(entry)
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise
                # else, file-not-found is ok, just skip

    return results


def _check_object_from_file(query, filepath, allow_custom, version):
    """
    Read a STIX object from the given file, and check it against the given
    filters.

    :param query: Iterable of filters
    :param filepath: Path to file to read
    :param allow_custom: Whether to allow custom properties as well unknown
        custom objects.
    :param version: Which STIX2 version to use. (e.g. "2.0", "2.1"). If None,
        use latest version.
    :return: The (parsed) STIX object, if the object passes the filters.  If
        not, None is returned.
    :raises TypeError: If the file had invalid JSON
    :raises IOError: If there are problems opening/reading the file
    :raises stix2.exceptions.STIXError: If there were problems creating a STIX
        object from the JSON
    """
    try:
        with open(filepath, "r") as f:
            stix_json = json.load(f)

    except ValueError:  # not a JSON file
        raise TypeError(
            "STIX JSON object at '{0}' could either not be parsed "
            "to JSON or was not valid STIX JSON".format(
                filepath))

    stix_obj = parse(stix_json, allow_custom, version)

    if stix_obj["type"] == "bundle":
        stix_obj = stix_obj["objects"][0]

    # check against other filters, add if match
    result = next(apply_common_filters([stix_obj], query), None)

    return result


def _search_versioned(query, type_path, auth_ids, allow_custom, version):
    """
    Searches the given directory, which contains data for STIX objects of a
    particular versioned type (i.e. not markings), and return any which match
    the query.

    :param query: The query to match against
    :param type_path: The directory with type-specific STIX object files
    :param auth_ids: Search optimization based on object ID
    :param allow_custom: Whether to allow custom properties as well unknown
        custom objects.
    :param version: Which STIX2 version to use. (e.g. "2.0", "2.1"). If None,
        use latest version.
    :return: A list of all matching objects
    :raises TypeError, stix2.exceptions.STIXError: If any objects had invalid
        content
    :raises IOError, OSError: If there were any problems opening/reading files
    """
    results = []
    id_dirs = _get_matching_dir_entries(type_path, auth_ids,
                                        stat.S_ISDIR)
    for id_dir in id_dirs:
        id_path = os.path.join(type_path, id_dir)

        # This leverages a more sophisticated function to do a simple thing:
        # get all the JSON files from a directory.  I guess it does give us
        # file type checking, ensuring we only get regular files.
        version_files = _get_matching_dir_entries(id_path, _AUTHSET_ANY,
                                                  stat.S_ISREG, ".json")
        for version_file in version_files:
            version_path = os.path.join(id_path, version_file)

            try:
                stix_obj = _check_object_from_file(query, version_path,
                                                   allow_custom, version)
                if stix_obj:
                    results.append(stix_obj)
            except IOError as e:
                if e.errno != errno.ENOENT:
                    raise
                # else, file-not-found is ok, just skip

    # For backward-compatibility, also search for plain files named after
    # object IDs, in the type directory.
    id_files = _get_matching_dir_entries(type_path, auth_ids, stat.S_ISREG,
                                         ".json")
    for id_file in id_files:
        id_path = os.path.join(type_path, id_file)

        try:
            stix_obj = _check_object_from_file(query, id_path, allow_custom,
                                               version)
            if stix_obj:
                results.append(stix_obj)
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise
            # else, file-not-found is ok, just skip

    return results


def _search_markings(query, markings_path, auth_ids, allow_custom, version):
    """
    Searches the given directory, which contains markings data, and return any
    which match the query.

    :param query: The query to match against
    :param markings_path: The directory with STIX markings files
    :param auth_ids: Search optimization based on object ID
    :param allow_custom: Whether to allow custom properties as well unknown
        custom objects.
    :param version: Which STIX2 version to use. (e.g. "2.0", "2.1"). If None,
        use latest version.
    :return: A list of all matching objects
    :raises TypeError, stix2.exceptions.STIXError: If any objects had invalid
        content
    :raises IOError, OSError: If there were any problems opening/reading files
    """
    results = []
    id_files = _get_matching_dir_entries(markings_path, auth_ids, stat.S_ISREG,
                                         ".json")
    for id_file in id_files:
        id_path = os.path.join(markings_path, id_file)

        try:
            stix_obj = _check_object_from_file(query, id_path, allow_custom,
                                               version)
            if stix_obj:
                results.append(stix_obj)
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise
            # else, file-not-found is ok, just skip

    return results


class FileSystemStore(DataStoreMixin):
    """Interface to a file directory of STIX objects.

    FileSystemStore is a wrapper around a paired FileSystemSink
    and FileSystemSource.

    Args:
        stix_dir (str): path to directory of STIX objects
        allow_custom (bool): whether to allow custom STIX content to be
            pushed/retrieved. Defaults to True for FileSystemSource side(retrieving data)
            and False for FileSystemSink side(pushing data). However, when
            parameter is supplied, it will be applied to both FileSystemSource
            and FileSystemSink.
        bundlify (bool): whether to wrap objects in bundles when saving them.
            Default: False.

    Attributes:
        source (FileSystemSource): FileSystemSource
        sink (FileSystemSink): FileSystemSink

    """
    def __init__(self, stix_dir, allow_custom=None, bundlify=False):
        if allow_custom is None:
            allow_custom_source = True
            allow_custom_sink = False
        else:
            allow_custom_sink = allow_custom_source = allow_custom

        super(FileSystemStore, self).__init__(
            source=FileSystemSource(stix_dir=stix_dir, allow_custom=allow_custom_source),
            sink=FileSystemSink(stix_dir=stix_dir, allow_custom=allow_custom_sink, bundlify=bundlify)
        )


class FileSystemSink(DataSink):
    """Interface for adding/pushing STIX objects to file directory of STIX
    objects.

    Can be paired with a FileSystemSource, together as the two
    components of a FileSystemStore.

    Args:
        stix_dir (str): path to directory of STIX objects.
        allow_custom (bool): Whether to allow custom STIX content to be
            added to the FileSystemSource. Default: False
        bundlify (bool): Whether to wrap objects in bundles when saving them.
            Default: False.

    """
    def __init__(self, stix_dir, allow_custom=False, bundlify=False):
        super(FileSystemSink, self).__init__()
        self._stix_dir = os.path.abspath(stix_dir)
        self.allow_custom = allow_custom
        self.bundlify = bundlify

        if not os.path.exists(self._stix_dir):
            raise ValueError("directory path for STIX data does not exist")

    @property
    def stix_dir(self):
        return self._stix_dir

    def _check_path_and_write(self, stix_obj):
        """Write the given STIX object to a file in the STIX file directory.
        """
        type_dir = os.path.join(self._stix_dir, stix_obj["type"])
        if is_marking(stix_obj):
            filename = stix_obj["id"]
            obj_dir = type_dir
        else:
            filename = _timestamp2filename(stix_obj["modified"])
            obj_dir = os.path.join(type_dir, stix_obj["id"])

        file_path = os.path.join(obj_dir, filename + ".json")

        if not os.path.exists(obj_dir):
            os.makedirs(obj_dir)

        if self.bundlify:
            stix_obj = Bundle(stix_obj, allow_custom=self.allow_custom)

        with open(file_path, "w") as f:
            f.write(str(stix_obj))

    def add(self, stix_data=None, version=None):
        """Add STIX objects to file directory.

        Args:
            stix_data (STIX object OR dict OR str OR list): valid STIX 2.0 content
                in a STIX object (or list of), dict (or list of), or a STIX 2.0
                json encoded string.
            version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
                None, use latest version.

        Note:
            ``stix_data`` can be a Bundle object, but each object in it will be
            saved separately; you will be able to retrieve any of the objects
            the Bundle contained, but not the Bundle itself.

        """
        if isinstance(stix_data, Bundle):
            # recursively add individual STIX objects
            for stix_obj in stix_data.get("objects", []):
                self.add(stix_obj, version=version)

        elif isinstance(stix_data, _STIXBase):
            # adding python STIX object
            self._check_path_and_write(stix_data)

        elif isinstance(stix_data, (str, dict)):
            stix_data = parse(stix_data, allow_custom=self.allow_custom, version=version)
            self.add(stix_data, version=version)

        elif isinstance(stix_data, list):
            # recursively add individual STIX objects
            for stix_obj in stix_data:
                self.add(stix_obj, version=version)

        else:
            raise TypeError("stix_data must be a STIX object (or list of), "
                            "JSON formatted STIX (or list of), "
                            "or a JSON formatted STIX bundle")


class FileSystemSource(DataSource):
    """Interface for searching/retrieving STIX objects from a STIX object file
    directory.

    Can be paired with a FileSystemSink, together as the two
    components of a FileSystemStore.

    Args:
        stix_dir (str): path to directory of STIX objects
        allow_custom (bool): Whether to allow custom STIX content to be
            added to the FileSystemSink. Default: True

    """
    def __init__(self, stix_dir, allow_custom=True):
        super(FileSystemSource, self).__init__()
        self._stix_dir = os.path.abspath(stix_dir)
        self.allow_custom = allow_custom

        if not os.path.exists(self._stix_dir):
            raise ValueError("directory path for STIX data does not exist: %s" % self._stix_dir)

    @property
    def stix_dir(self):
        return self._stix_dir

    def get(self, stix_id, version=None, _composite_filters=None):
        """Retrieve STIX object from file directory via STIX ID.

        Args:
            stix_id (str): The STIX ID of the STIX object to be retrieved.
            _composite_filters (FilterSet): collection of filters passed from the parent
                CompositeDataSource, not user supplied
            version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
                None, use latest version.

        Returns:
            (STIX object): STIX object that has the supplied STIX ID.
                The STIX object is loaded from its json file, parsed into
                a python STIX object and then returned

        """
        all_data = self.all_versions(stix_id, version=version, _composite_filters=_composite_filters)

        if all_data:
            if is_marking(stix_id):
                # Markings are unversioned; there shouldn't be more than one
                # result.
                stix_obj = all_data[0]
            else:
                stix_obj = sorted(all_data, key=lambda k: k['modified'])[-1]
        else:
            stix_obj = None

        return stix_obj

    def all_versions(self, stix_id, version=None, _composite_filters=None):
        """Retrieve STIX object from file directory via STIX ID, all versions.

        Note: Since FileSystem sources/sinks don't handle multiple versions
        of a STIX object, this operation is unnecessary. Pass call to get().

        Args:
            stix_id (str): The STIX ID of the STIX objects to be retrieved.
            _composite_filters (FilterSet): collection of filters passed from the parent
                CompositeDataSource, not user supplied
            version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
                None, use latest version.

        Returns:
            (list): of STIX objects that has the supplied STIX ID.
                The STIX objects are loaded from their json files, parsed into
                a python STIX objects and then returned

        """
        query = [Filter("id", "=", stix_id)]
        return self.query(query, version=version, _composite_filters=_composite_filters)

    def query(self, query=None, version=None, _composite_filters=None):
        """Search and retrieve STIX objects based on the complete query.

        A "complete query" includes the filters from the query, the filters
        attached to this FileSystemSource, and any filters passed from a
        CompositeDataSource (i.e. _composite_filters).

        Args:
            query (list): list of filters to search on
            _composite_filters (FilterSet): collection of filters passed from the
                CompositeDataSource, not user supplied
            version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
                None, use latest version.

        Returns:
            (list): list of STIX objects that matches the supplied
                query. The STIX objects are loaded from their json files,
                parsed into a python STIX objects and then returned.

        """

        all_data = []

        query = FilterSet(query)

        # combine all query filters
        if self.filters:
            query.add(self.filters)
        if _composite_filters:
            query.add(_composite_filters)

        auth_types, auth_ids = _find_search_optimizations(query)

        type_dirs = _get_matching_dir_entries(self._stix_dir, auth_types,
                                              stat.S_ISDIR)
        for type_dir in type_dirs:
            type_path = os.path.join(self._stix_dir, type_dir)

            if type_dir == "marking-definition":
                type_results = _search_markings(query, type_path, auth_ids,
                                                self.allow_custom, version)
            else:
                type_results = _search_versioned(query, type_path, auth_ids,
                                                 self.allow_custom, version)

            all_data.extend(type_results)

        return all_data
