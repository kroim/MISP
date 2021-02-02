"""STIX 2 Common Data Types and Properties."""

from collections import OrderedDict
import copy

from ..base import _cls_init, _STIXBase
from ..markings import _MarkingsMixin
from ..properties import (HashesProperty, IDProperty, ListProperty, Property,
                          ReferenceProperty, SelectorProperty, StringProperty,
                          TimestampProperty, TypeProperty)
from ..utils import NOW, _get_dict


class ExternalReference(_STIXBase):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709261>`__.
    """

    _properties = OrderedDict()
    _properties.update([
        ('source_name', StringProperty(required=True)),
        ('description', StringProperty()),
        ('url', StringProperty()),
        ('hashes', HashesProperty()),
        ('external_id', StringProperty()),
    ])

    def _check_object_constraints(self):
        super(ExternalReference, self)._check_object_constraints()
        self._check_at_least_one_property(["description", "external_id", "url"])


class KillChainPhase(_STIXBase):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709267>`__.
    """

    _properties = OrderedDict()
    _properties.update([
        ('kill_chain_name', StringProperty(required=True)),
        ('phase_name', StringProperty(required=True)),
    ])


class GranularMarking(_STIXBase):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709290>`__.
    """

    _properties = OrderedDict()
    _properties.update([
        ('marking_ref', ReferenceProperty(required=True, type="marking-definition")),
        ('selectors', ListProperty(SelectorProperty, required=True)),
    ])


class TLPMarking(_STIXBase):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709287>`__.
    """

    # TODO: don't allow the creation of any other TLPMarkings than the ones below
    _type = 'tlp'
    _properties = OrderedDict()
    _properties.update([
        ('tlp', StringProperty(required=True))
    ])


class StatementMarking(_STIXBase):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709286>`__.
    """

    _type = 'statement'
    _properties = OrderedDict()
    _properties.update([
        ('statement', StringProperty(required=True))
    ])

    def __init__(self, statement=None, **kwargs):
        # Allow statement as positional args.
        if statement and not kwargs.get('statement'):
            kwargs['statement'] = statement

        super(StatementMarking, self).__init__(**kwargs)


class MarkingProperty(Property):
    """Represent the marking objects in the ``definition`` property of
    marking-definition objects.
    """

    def clean(self, value):
        if type(value) in OBJ_MAP_MARKING.values():
            return value
        else:
            raise ValueError("must be a Statement, TLP Marking or a registered marking.")


class MarkingDefinition(_STIXBase, _MarkingsMixin):
    """For more detailed information on this object's properties, see
    `the STIX 2.0 specification <http://docs.oasis-open.org/cti/stix/v2.0/cs01/part1-stix-core/stix-v2.0-cs01-part1-stix-core.html#_Toc496709284>`__.
    """

    _type = 'marking-definition'
    _properties = OrderedDict()
    _properties.update([
        ('type', TypeProperty(_type)),
        ('id', IDProperty(_type)),
        ('created_by_ref', ReferenceProperty(type="identity")),
        ('created', TimestampProperty(default=lambda: NOW)),
        ('external_references', ListProperty(ExternalReference)),
        ('object_marking_refs', ListProperty(ReferenceProperty(type="marking-definition"))),
        ('granular_markings', ListProperty(GranularMarking)),
        ('definition_type', StringProperty(required=True)),
        ('definition', MarkingProperty(required=True)),
    ])

    def __init__(self, **kwargs):
        if set(('definition_type', 'definition')).issubset(kwargs.keys()):
            # Create correct marking type object
            try:
                marking_type = OBJ_MAP_MARKING[kwargs['definition_type']]
            except KeyError:
                raise ValueError("definition_type must be a valid marking type")

            if marking_type == TLPMarking:
                # TLP instances in the spec have millisecond precision unlike other markings
                self._properties = copy.deepcopy(self._properties)
                self._properties.update([
                    ('created', TimestampProperty(default=lambda: NOW, precision='millisecond')),
                ])

            if not isinstance(kwargs['definition'], marking_type):
                defn = _get_dict(kwargs['definition'])
                kwargs['definition'] = marking_type(**defn)
            interoperability = kwargs.get('interoperability', False)
            self._properties['id'].interoperability = interoperability
            if kwargs.get('created_by_ref'):
                self._properties['created_by_ref'].interoperability = interoperability
            if kwargs.get('object_marking_refs'):
                self._properties['object_marking_refs'].contained.interoperability = interoperability

        super(MarkingDefinition, self).__init__(**kwargs)


OBJ_MAP_MARKING = {
    'tlp': TLPMarking,
    'statement': StatementMarking,
}


def _register_marking(cls):
    """Register a custom STIX Marking Definition type.
    """
    OBJ_MAP_MARKING[cls._type] = cls
    return cls


def CustomMarking(type='x-custom-marking', properties=None):
    """Custom STIX Marking decorator.

    Example:
        >>> @CustomMarking('x-custom-marking', [
        ...     ('property1', StringProperty(required=True)),
        ...     ('property2', IntegerProperty()),
        ... ])
        ... class MyNewMarkingObjectType():
        ...     pass

    """
    def custom_builder(cls):

        class _Custom(cls, _STIXBase):
            _type = type
            _properties = OrderedDict()

            if not properties or not isinstance(properties, list):
                raise ValueError("Must supply a list, containing tuples. For example, [('property1', IntegerProperty())]")

            _properties.update(properties)

            def __init__(self, **kwargs):
                _STIXBase.__init__(self, **kwargs)
                _cls_init(cls, self, kwargs)

        _register_marking(_Custom)
        return _Custom

    return custom_builder


TLP_WHITE = MarkingDefinition(
    id="marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
    created="2017-01-20T00:00:00.000Z",
    definition_type="tlp",
    definition=TLPMarking(tlp="white")
)

TLP_GREEN = MarkingDefinition(
    id="marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
    created="2017-01-20T00:00:00.000Z",
    definition_type="tlp",
    definition=TLPMarking(tlp="green")
)

TLP_AMBER = MarkingDefinition(
    id="marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
    created="2017-01-20T00:00:00.000Z",
    definition_type="tlp",
    definition=TLPMarking(tlp="amber")
)

TLP_RED = MarkingDefinition(
    id="marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed",
    created="2017-01-20T00:00:00.000Z",
    definition_type="tlp",
    definition=TLPMarking(tlp="red")
)
