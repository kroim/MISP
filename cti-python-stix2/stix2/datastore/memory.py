"""
Python STIX 2.0 Memory Source/Sink
"""

import itertools
import json
import os

from stix2.base import _STIXBase
from stix2.core import Bundle, parse
from stix2.datastore import DataSink, DataSource, DataStoreMixin
from stix2.datastore.filters import FilterSet, apply_common_filters
from stix2.utils import is_marking


def _add(store, stix_data=None, allow_custom=True, version=None):
    """Add STIX objects to MemoryStore/Sink.

    Adds STIX objects to an in-memory dictionary for fast lookup.
    Recursive function, breaks down STIX Bundles and lists.

    Args:
        stix_data (list OR dict OR STIX object): STIX objects to be added
        version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
            None, use latest version.

    """
    if isinstance(stix_data, list):
        # STIX objects are in a list- recurse on each object
        for stix_obj in stix_data:
            _add(store, stix_obj, allow_custom, version)

    elif stix_data["type"] == "bundle":
        # adding a json bundle - so just grab STIX objects
        for stix_obj in stix_data.get("objects", []):
            _add(store, stix_obj, allow_custom, version)

    else:
        # Adding a single non-bundle object
        if isinstance(stix_data, _STIXBase):
            stix_obj = stix_data
        else:
            stix_obj = parse(stix_data, allow_custom, version)

        # Map ID directly to the object, if it is a marking.  Otherwise,
        # map to a family, so we can track multiple versions.
        if is_marking(stix_obj):
            store._data[stix_obj["id"]] = stix_obj

        else:
            if stix_obj["id"] in store._data:
                obj_family = store._data[stix_obj["id"]]
            else:
                obj_family = _ObjectFamily()
                store._data[stix_obj["id"]] = obj_family

            obj_family.add(stix_obj)


class _ObjectFamily(object):
    """
    An internal implementation detail of memory sources/sinks/stores.
    Represents a "family" of STIX objects: all objects with a particular
    ID.  (I.e. all versions.)  The latest version is also tracked so that it
    can be obtained quickly.
    """
    def __init__(self):
        self.all_versions = {}
        self.latest_version = None

    def add(self, obj):
        self.all_versions[obj["modified"]] = obj
        if self.latest_version is None or \
                obj["modified"] > self.latest_version["modified"]:
            self.latest_version = obj

    def __str__(self):
        return "<<{}; latest={}>>".format(self.all_versions,
                                          self.latest_version["modified"])

    def __repr__(self):
        return str(self)


class MemoryStore(DataStoreMixin):
    """Interface to an in-memory dictionary of STIX objects.

    MemoryStore is a wrapper around a paired MemorySink and MemorySource.

    Note: It doesn't make sense to create a MemoryStore by passing
    in existing MemorySource and MemorySink because there could
    be data concurrency issues. As well, just as easy to create new MemoryStore.

    Args:
        stix_data (list OR dict OR STIX object): STIX content to be added
        allow_custom (bool): whether to allow custom STIX content.
            Only applied when export/input functions called, i.e.
            load_from_file() and save_to_file(). Defaults to True.
        version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
            None, use latest version.

    Attributes:
        _data (dict): the in-memory dict that holds STIX objects
        source (MemorySource): MemorySource
        sink (MemorySink): MemorySink

    """
    def __init__(self, stix_data=None, allow_custom=True, version=None):
        self._data = {}

        if stix_data:
            _add(self, stix_data, allow_custom, version=version)

        super(MemoryStore, self).__init__(
            source=MemorySource(stix_data=self._data, allow_custom=allow_custom, version=version, _store=True),
            sink=MemorySink(stix_data=self._data, allow_custom=allow_custom, version=version, _store=True)
        )

    def save_to_file(self, *args, **kwargs):
        """Write SITX objects from in-memory dictionary to JSON file, as a STIX
        Bundle.

        Args:
            file_path (str): file path to write STIX data to

        """
        return self.sink.save_to_file(*args, **kwargs)

    def load_from_file(self, *args, **kwargs):
        """Load STIX data from JSON file.

        File format is expected to be a single JSON
        STIX object or JSON STIX bundle.

        Args:
            file_path (str): file path to load STIX data from
            version (str): Which STIX2 version to use. (e.g. "2.0", "2.1"). If
                None, use latest version.

        """
        return self.source.load_from_file(*args, **kwargs)


class MemorySink(DataSink):
    """Interface for adding/pushing STIX objects to an in-memory dictionary.

    Designed to be paired with a MemorySource, together as the two
    components of a MemoryStore.

    Args:
        stix_data (dict OR list): valid STIX 2.0 content in
            bundle or a list.
        _store (bool): whether the MemorySink is a part of a MemoryStore,
            in which case "stix_data" is a direct reference to
            shared memory with DataSource. Not user supplied
        allow_custom (bool): whether to allow custom objects/properties
            when exporting STIX content to file.
            Default: True.

    Attributes:
        _data (dict): the in-memory dict that holds STIX objects.
            If part of a MemoryStore, the dict is shared with a MemorySource

    """
    def __init__(self, stix_data=None, allow_custom=True, version=None, _store=False):
        super(MemorySink, self).__init__()
        self.allow_custom = allow_custom

        if _store:
            self._data = stix_data
        else:
            self._data = {}
            if stix_data:
                _add(self, stix_data, allow_custom, version=version)

    def add(self, stix_data, version=None):
        _add(self, stix_data, self.allow_custom, version)
    add.__doc__ = _add.__doc__

    def save_to_file(self, file_path):
        file_path = os.path.abspath(file_path)

        all_objs = itertools.chain.from_iterable(
            value.all_versions.values() if isinstance(value, _ObjectFamily)
            else [value]
            for value in self._data.values()
        )

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        with open(file_path, "w") as f:
            f.write(str(Bundle(list(all_objs), allow_custom=self.allow_custom)))
    save_to_file.__doc__ = MemoryStore.save_to_file.__doc__


class MemorySource(DataSource):
    """Interface for searching/retrieving STIX objects from an in-memory
    dictionary.

    Designed to be paired with a MemorySink, together as the two
    components of a MemoryStore.

    Args:
        stix_data (dict OR list OR STIX object): valid STIX 2.0 content in
            bundle or list.
        _store (bool): if the MemorySource is a part of a MemoryStore,
            in which case "stix_data" is a direct reference to shared
            memory with DataSink. Not user supplied
        allow_custom (bool): whether to allow custom objects/properties
            when importing STIX content from file.
            Default: True.

    Attributes:
        _data (dict): the in-memory dict that holds STIX objects.
            If part of a MemoryStore, the dict is shared with a MemorySink

    """
    def __init__(self, stix_data=None, allow_custom=True, version=None, _store=False):
        super(MemorySource, self).__init__()
        self.allow_custom = allow_custom

        if _store:
            self._data = stix_data
        else:
            self._data = {}
            if stix_data:
                _add(self, stix_data, allow_custom, version=version)

    def get(self, stix_id, _composite_filters=None):
        """Retrieve STIX object from in-memory dict via STIX ID.

        Args:
            stix_id (str): The STIX ID of the STIX object to be retrieved.
            _composite_filters (FilterSet): collection of filters passed from the parent
                CompositeDataSource, not user supplied

        Returns:
            (STIX object): STIX object that has the supplied ID.

        """
        stix_obj = None

        if is_marking(stix_id):
            stix_obj = self._data.get(stix_id)
        else:
            object_family = self._data.get(stix_id)
            if object_family:
                stix_obj = object_family.latest_version

        if stix_obj:
            all_filters = list(
                itertools.chain(
                    _composite_filters or [],
                    self.filters
                )
            )

            stix_obj = next(apply_common_filters([stix_obj], all_filters), None)

        return stix_obj

    def all_versions(self, stix_id, _composite_filters=None):
        """Retrieve STIX objects from in-memory dict via STIX ID, all versions of it

        Note: Since Memory sources/sinks don't handle multiple versions of a
        STIX object, this operation is unnecessary. Translate call to get().

        Args:
            stix_id (str): The STIX ID of the STIX 2 object to retrieve.
            _composite_filters (FilterSet): collection of filters passed from the parent
                CompositeDataSource, not user supplied

        Returns:
            (list): list of STIX objects that have the supplied ID.

        """
        results = []
        stix_objs_to_filter = None
        if is_marking(stix_id):
            stix_obj = self._data.get(stix_id)
            if stix_obj:
                stix_objs_to_filter = [stix_obj]
        else:
            object_family = self._data.get(stix_id)
            if object_family:
                stix_objs_to_filter = object_family.all_versions.values()

        if stix_objs_to_filter:
            all_filters = list(
                itertools.chain(
                    _composite_filters or [],
                    self.filters
                )
            )

            results.extend(
                apply_common_filters(stix_objs_to_filter, all_filters)
            )

        return results

    def query(self, query=None, _composite_filters=None):
        """Search and retrieve STIX objects based on the complete query.

        A "complete query" includes the filters from the query, the filters
        attached to this MemorySource, and any filters passed from a
        CompositeDataSource (i.e. _composite_filters).

        Args:
            query (list): list of filters to search on
            _composite_filters (FilterSet): collection of filters passed from the
                CompositeDataSource, not user supplied

        Returns:
            (list): list of STIX objects that match the supplied query.

        """
        query = FilterSet(query)

        # combine all query filters
        if self.filters:
            query.add(self.filters)
        if _composite_filters:
            query.add(_composite_filters)

        all_objs = itertools.chain.from_iterable(
            value.all_versions.values() if isinstance(value, _ObjectFamily)
            else [value]
            for value in self._data.values()
        )

        # Apply STIX common property filters.
        all_data = list(apply_common_filters(all_objs, query))

        return all_data

    def load_from_file(self, file_path, version=None):
        with open(os.path.abspath(file_path), "r") as f:
            stix_data = json.load(f)

        # Override user version selection if loading a bundle
        if stix_data["type"] == "bundle":
            version = stix_data["spec_version"]

        _add(self, stix_data, self.allow_custom, version)
    load_from_file.__doc__ = MemoryStore.load_from_file.__doc__
