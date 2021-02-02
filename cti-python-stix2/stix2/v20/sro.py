"""STIX 2.0 Relationship Objects."""

from collections import OrderedDict

from ..base import _STIXBase
from ..markings import _MarkingsMixin
from ..properties import (BooleanProperty, IDProperty, IntegerProperty,
                          ListProperty, ReferenceProperty, StringProperty,
                          TimestampProperty, TypeProperty)
from ..utils import NOW
from .common import ExternalReference, GranularMarking


class STIXRelationshipObject(_STIXBase, _MarkingsMixin):
    def __init__(self, *args, **kwargs):
        interoperability = kwargs.get('interoperability', False)
        self.__interoperability = interoperability
        self._properties['id'].interoperability = interoperability
        if kwargs.get('created_by_ref'):
            self._properties['created_by_ref'].interoperability = interoperability
        if kwargs.get('object_marking_refs'):
            self._properties['object_marking_refs'].contained.interoperability = interoperability

        super(STIXRelationshipObject, self).__init__(*args, **kwargs)


class Relationship(STIXRelationshipObject):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part2-stix-objects/stix-v2.0-cs01-part2-stix-objects.html#_Toc496714340>`__.
    """

    _type = 'relationship'
    _properties = OrderedDict()
    _properties.update([
        ('type', TypeProperty(_type)),
        ('id', IDProperty(_type)),
        ('created_by_ref', ReferenceProperty(type="identity")),
        ('created', TimestampProperty(default=lambda: NOW, precision='millisecond')),
        ('modified', TimestampProperty(default=lambda: NOW, precision='millisecond')),
        ('relationship_type', StringProperty(required=True)),
        ('description', StringProperty()),
        ('source_ref', ReferenceProperty(required=True)),
        ('target_ref', ReferenceProperty(required=True)),
        ('revoked', BooleanProperty(default=lambda: False)),
        ('labels', ListProperty(StringProperty)),
        ('external_references', ListProperty(ExternalReference)),
        ('object_marking_refs', ListProperty(ReferenceProperty(type="marking-definition"))),
        ('granular_markings', ListProperty(GranularMarking)),
    ])

    # Explicitly define the first three kwargs to make readable Relationship declarations.
    def __init__(self, source_ref=None, relationship_type=None,
                 target_ref=None, **kwargs):
        # Allow (source_ref, relationship_type, target_ref) as positional args.
        if source_ref and not kwargs.get('source_ref'):
            kwargs['source_ref'] = source_ref
        if relationship_type and not kwargs.get('relationship_type'):
            kwargs['relationship_type'] = relationship_type
        if target_ref and not kwargs.get('target_ref'):
            kwargs['target_ref'] = target_ref
        interoperability = kwargs.get('interoperability', False)
        self._properties['source_ref'].interoperability = interoperability
        self._properties['target_ref'].interoperability = interoperability

        super(Relationship, self).__init__(**kwargs)


class Sighting(STIXRelationshipObject):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part2-stix-objects/stix-v2.0-cs01-part2-stix-objects.html#_Toc496714343>`__.
    """

    _type = 'sighting'
    _properties = OrderedDict()
    _properties.update([
        ('type', TypeProperty(_type)),
        ('id', IDProperty(_type)),
        ('created_by_ref', ReferenceProperty(type="identity")),
        ('created', TimestampProperty(default=lambda: NOW, precision='millisecond')),
        ('modified', TimestampProperty(default=lambda: NOW, precision='millisecond')),
        ('first_seen', TimestampProperty()),
        ('last_seen', TimestampProperty()),
        ('count', IntegerProperty()),
        ('sighting_of_ref', ReferenceProperty(required=True)),
        ('observed_data_refs', ListProperty(ReferenceProperty(type="observed-data"))),
        ('where_sighted_refs', ListProperty(ReferenceProperty(type="identity"))),
        ('summary', BooleanProperty(default=lambda: False)),
        ('revoked', BooleanProperty(default=lambda: False)),
        ('labels', ListProperty(StringProperty)),
        ('external_references', ListProperty(ExternalReference)),
        ('object_marking_refs', ListProperty(ReferenceProperty(type="marking-definition"))),
        ('granular_markings', ListProperty(GranularMarking)),
    ])

    # Explicitly define the first kwargs to make readable Sighting declarations.
    def __init__(self, sighting_of_ref=None, **kwargs):
        # Allow sighting_of_ref as a positional arg.
        if sighting_of_ref and not kwargs.get('sighting_of_ref'):
            kwargs['sighting_of_ref'] = sighting_of_ref
        interoperability = kwargs.get('interoperability', False)
        self._properties['sighting_of_ref'].interoperability = interoperability
        if kwargs.get('observed_data_refs'):
            self._properties['observed_data_refs'].contained.interoperability = interoperability
        if kwargs.get('where_sighted_refs'):
            self._properties['where_sighted_refs'].contained.interoperability = interoperability

        super(Sighting, self).__init__(**kwargs)
