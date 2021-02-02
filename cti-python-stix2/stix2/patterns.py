"""Classes to aid in working with the STIX 2 patterning language.
"""

import base64
import binascii
import datetime
import re

from .utils import parse_into_datetime


def escape_quotes_and_backslashes(s):
    return s.replace(u'\\', u'\\\\').replace(u"'", u"\\'")


class _Constant(object):
    pass


class StringConstant(_Constant):
    """Pattern string constant

    Args:
        value (str): string value
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s'" % escape_quotes_and_backslashes(self.value)


class TimestampConstant(_Constant):
    """Pattern timestamp constant

    Args:
        value (datetime.datetime OR str): if string, must be a timestamp string
    """
    def __init__(self, value):
        try:
            self.value = parse_into_datetime(value)
        except Exception:
            raise ValueError("Must be a datetime object or timestamp string.")

    def __str__(self):
        return "t%s" % repr(self.value)


class IntegerConstant(_Constant):
    """Pattern interger constant

    Args:
        value (int): integer value
    """
    def __init__(self, value):
        try:
            self.value = int(value)
        except Exception:
            raise ValueError("must be an integer.")

    def __str__(self):
        return "%s" % self.value


class FloatConstant(_Constant):
    def __init__(self, value):
        try:
            self.value = float(value)
        except Exception:
            raise ValueError("must be a float.")

    def __str__(self):
        return "%s" % self.value


class BooleanConstant(_Constant):
    """Pattern boolean constant

    Args:
       value (str OR int):
           (str) 'true', 't' for True; 'false', 'f' for False
           (int) 1 for True; 0 for False
    """
    def __init__(self, value):
        if isinstance(value, bool):
            self.value = value
            return

        trues = ['true', 't']
        falses = ['false', 'f']
        try:
            if value.lower() in trues:
                self.value = True
                return
            elif value.lower() in falses:
                self.value = False
                return
        except AttributeError:
            if value == 1:
                self.value = True
                return
            elif value == 0:
                self.value = False
                return

        raise ValueError("must be a boolean value.")

    def __str__(self):
        return str(self.value).lower()


_HASH_REGEX = {
    "MD5": ("^[a-fA-F0-9]{32}$", "MD5"),
    "MD6": ("^[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{56}|[a-fA-F0-9]{64}|[a-fA-F0-9]{96}|[a-fA-F0-9]{128}$", "MD6"),
    "RIPEMD160": ("^[a-fA-F0-9]{40}$", "RIPEMD-160"),
    "SHA1": ("^[a-fA-F0-9]{40}$", "SHA-1"),
    "SHA224": ("^[a-fA-F0-9]{56}$", "SHA-224"),
    "SHA256": ("^[a-fA-F0-9]{64}$", "SHA-256"),
    "SHA384": ("^[a-fA-F0-9]{96}$", "SHA-384"),
    "SHA512": ("^[a-fA-F0-9]{128}$", "SHA-512"),
    "SHA3224": ("^[a-fA-F0-9]{56}$", "SHA3-224"),
    "SHA3256": ("^[a-fA-F0-9]{64}$", "SHA3-256"),
    "SHA3384": ("^[a-fA-F0-9]{96}$", "SHA3-384"),
    "SHA3512": ("^[a-fA-F0-9]{128}$", "SHA3-512"),
    "SSDEEP": ("^[a-zA-Z0-9/+:.]{1,128}$", "ssdeep"),
    "WHIRLPOOL": ("^[a-fA-F0-9]{128}$", "WHIRLPOOL"),
}


class HashConstant(StringConstant):
    """Pattern hash constant

    Args:
        value (str): hash value
        type (str): hash algorithm name. Supported hash algorithms:
            "MD5", "MD6", RIPEMD160", "SHA1", "SHA224", "SHA256",
            "SHA384", "SHA512", "SHA3224", "SHA3256", "SHA3384",
            "SHA3512", "SSDEEP", "WHIRLPOOL"
    """
    def __init__(self, value, type):
        key = type.upper().replace('-', '')
        if key in _HASH_REGEX:
            vocab_key = _HASH_REGEX[key][1]
            if not re.match(_HASH_REGEX[key][0], value):
                raise ValueError("'%s' is not a valid %s hash" % (value, vocab_key))
            self.value = value


class BinaryConstant(_Constant):
    """Pattern binary constant

    Args:
        value (str): base64 encoded string value
    """
    def __init__(self, value):
        try:
            base64.b64decode(value)
            self.value = value
        except (binascii.Error, TypeError):
            raise ValueError("must contain a base64 encoded string")

    def __str__(self):
        return "b'%s'" % self.value


class HexConstant(_Constant):
    """Pattern hexadecimal constant

    Args:
        value (str): hexadecimal value
    """
    def __init__(self, value):
        if not re.match('^([a-fA-F0-9]{2})+$', value):
            raise ValueError("must contain an even number of hexadecimal characters")
        self.value = value

    def __str__(self):
        return "h'%s'" % self.value


class ListConstant(_Constant):
    """Pattern list constant

    Args:
        value (list): list of values
    """
    def __init__(self, values):
        self.value = values

    def __str__(self):
        return "(" + ", ".join([("%s" % make_constant(x)) for x in self.value]) + ")"


def make_constant(value):
    """Convert value to Pattern constant, best effort attempt
    at determining root value type and corresponding conversion

    Args:
        value: value to convert to Pattern constant
    """
    if isinstance(value, _Constant):
        return value

    try:
        return parse_into_datetime(value)
    except ValueError:
        pass

    if isinstance(value, str):
        return StringConstant(value)
    elif isinstance(value, bool):
        return BooleanConstant(value)
    elif isinstance(value, int):
        return IntegerConstant(value)
    elif isinstance(value, float):
        return FloatConstant(value)
    elif isinstance(value, list):
        return ListConstant(value)
    else:
        raise ValueError("Unable to create a constant from %s" % value)


class _ObjectPathComponent(object):
    @staticmethod
    def create_ObjectPathComponent(component_name):
        if component_name.endswith("_ref"):
            return ReferenceObjectPathComponent(component_name)
        elif component_name.find("[") != -1:
            parse1 = component_name.split("[")
            return ListObjectPathComponent(parse1[0], parse1[1][:-1])
        else:
            return BasicObjectPathComponent(component_name)


class BasicObjectPathComponent(_ObjectPathComponent):
    """Basic object path component (for an observation or expression)

    By "Basic", implies that the object path component is not a
    list, object reference or futher referenced property, i.e. terminal
    component

    Args:
        property_name (str): object property name
        is_key (bool): is dictionary key, default: False
    """
    def __init__(self, property_name, is_key=False):
        self.property_name = property_name
        # TODO: set is_key to True if this component is a dictionary key
        # self.is_key = is_key

    def __str__(self):
        return self.property_name


class ListObjectPathComponent(_ObjectPathComponent):
    """List object path component (for an observation or expression)

    Args:
        property_name (str): list object property name
        index (int): index of the list property's value that is specified
    """
    def __init__(self, property_name, index):
        self.property_name = property_name
        self.index = index

    def __str__(self):
        return "%s[%s]" % (self.property_name, self.index)


class ReferenceObjectPathComponent(_ObjectPathComponent):
    """Reference object path component (for an observation or expression)

    Args:
        reference_property_name (str): reference object property name
    """
    def __init__(self, reference_property_name):
        self.property_name = reference_property_name

    def __str__(self):
        return self.property_name


class ObjectPath(object):
    """Pattern operand object (property) path

    Args:
        object_type_name (str): name of object type for corresponding object path component
        property_path (_ObjectPathComponent OR str): object path
    """
    def __init__(self, object_type_name, property_path):
        self.object_type_name = object_type_name
        self.property_path = [x if isinstance(x, _ObjectPathComponent) else
                              _ObjectPathComponent.create_ObjectPathComponent(x)
                              for x in property_path]

    def __str__(self):
        return "%s:%s" % (self.object_type_name, ".".join(["%s" % x for x in self.property_path]))

    def merge(self, other):
        """Extend the object property with that of the supplied object property path"""
        self.property_path.extend(other.property_path)
        return self

    @staticmethod
    def make_object_path(lhs):
        """Create ObjectPath from string encoded object path

        Args:
            lhs (str): object path of left-hand-side component of expression
        """
        path_as_parts = lhs.split(":")
        return ObjectPath(path_as_parts[0], path_as_parts[1].split("."))


class _PatternExpression(object):
    pass


class _ComparisonExpression(_PatternExpression):
    """Pattern Comparison Expression

    Args:
        operator (str): operator of comparison expression
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, operator, lhs, rhs, negated=False):
        if operator == "=" and isinstance(rhs, (ListConstant, list)):
            self.operator = "IN"
        else:
            self.operator = operator
        if isinstance(lhs, ObjectPath):
            self.lhs = lhs
        else:
            self.lhs = ObjectPath.make_object_path(lhs)
        if isinstance(rhs, _Constant):
            self.rhs = rhs
        else:
            self.rhs = make_constant(rhs)
        self.negated = negated
        self.root_type = self.lhs.object_type_name

    def __str__(self):
        if self.negated:
            return "%s NOT %s %s" % (self.lhs, self.operator, self.rhs)
        else:
            return "%s %s %s" % (self.lhs, self.operator, self.rhs)


class EqualityComparisonExpression(_ComparisonExpression):
    """Pattern Equality Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(EqualityComparisonExpression, self).__init__("=", lhs, rhs, negated)


class GreaterThanComparisonExpression(_ComparisonExpression):
    """Pattern Greater-than Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(GreaterThanComparisonExpression, self).__init__(">", lhs, rhs, negated)


class LessThanComparisonExpression(_ComparisonExpression):
    """Pattern Less-than Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(LessThanComparisonExpression, self).__init__("<", lhs, rhs, negated)


class GreaterThanEqualComparisonExpression(_ComparisonExpression):
    """Pattern Greater-Than-or-Equal-to Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(GreaterThanEqualComparisonExpression, self).__init__(">=", lhs, rhs, negated)


class LessThanEqualComparisonExpression(_ComparisonExpression):
    """Pattern Less-Than-or-Equal-to Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """

    def __init__(self, lhs, rhs, negated=False):
        super(LessThanEqualComparisonExpression, self).__init__("<=", lhs, rhs, negated)


class InComparisonExpression(_ComparisonExpression):
    """'in' Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(InComparisonExpression, self).__init__("IN", lhs, rhs, negated)


class LikeComparisonExpression(_ComparisonExpression):
    """'like' Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """

    def __init__(self, lhs, rhs, negated=False):
        super(LikeComparisonExpression, self).__init__("LIKE", lhs, rhs, negated)


class MatchesComparisonExpression(_ComparisonExpression):
    """'Matches' Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(MatchesComparisonExpression, self).__init__("MATCHES", lhs, rhs, negated)


class IsSubsetComparisonExpression(_ComparisonExpression):
    """ 'is subset' Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(IsSubsetComparisonExpression, self).__init__("ISSUBSET", lhs, rhs, negated)


class IsSupersetComparisonExpression(_ComparisonExpression):
    """ 'is super set' Comparison Expression

    Args:
        lhs (ObjectPath OR str): object path of left-hand-side component of expression
        rhs (ObjectPath OR str): object path of right-hand-side component of expression
        negated (bool): comparison expression negated. Default: False
    """
    def __init__(self, lhs, rhs, negated=False):
        super(IsSupersetComparisonExpression, self).__init__("ISSUPERSET", lhs, rhs, negated)


class _BooleanExpression(_PatternExpression):
    """Boolean Pattern Expression

    Args:
        operator (str): boolean operator
        operands (list): boolean operands
    """
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = []
        for arg in operands:
            if not hasattr(self, "root_type"):
                self.root_type = arg.root_type
            elif self.root_type and (self.root_type != arg.root_type) and operator == "AND":
                raise ValueError("All operands to an 'AND' expression must have the same object type")
            elif self.root_type and (self.root_type != arg.root_type):
                self.root_type = None
            self.operands.append(arg)

    def __str__(self):
        sub_exprs = []
        for o in self.operands:
            sub_exprs.append(str(o))
        return (" " + self.operator + " ").join(sub_exprs)


class AndBooleanExpression(_BooleanExpression):
    """'AND' Boolean Pattern Expression. Only use if both operands are of
    the same root object.

    Args:
        operands (list): AND operands
    """
    def __init__(self, operands):
        super(AndBooleanExpression, self).__init__("AND", operands)


class OrBooleanExpression(_BooleanExpression):
    """'OR' Boolean Pattern Expression. Only use if both operands are of the same root object

    Args:
        operands (list): OR operands
    """
    def __init__(self, operands):
        super(OrBooleanExpression, self).__init__("OR", operands)


class ObservationExpression(_PatternExpression):
    """Observation Expression

    Args:
        operand (str): observation expression operand
    """
    def __init__(self, operand):
        self.operand = operand

    def __str__(self):
        return "[%s]" % self.operand


class _CompoundObservationExpression(_PatternExpression):
    """Compound Observation Expression

    Args:
        operator (str): compound observation operator
        operands (str): compound observation operands
    """
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __str__(self):
        sub_exprs = []
        for o in self.operands:
            sub_exprs.append("%s" % o)
        return (" " + self.operator + " ").join(sub_exprs)


class AndObservationExpression(_CompoundObservationExpression):
    """'AND' Compound Observation Pattern Expression

    Args:
        operands (str): compound observation operands
    """
    def __init__(self, operands):
        super(AndObservationExpression, self).__init__("AND", operands)


class OrObservationExpression(_CompoundObservationExpression):
    """Pattern 'OR' Compound Observation Expression

    Args:
        operands (str): compound observation operands
    """
    def __init__(self, operands):
        super(OrObservationExpression, self).__init__("OR", operands)


class FollowedByObservationExpression(_CompoundObservationExpression):
    """Pattern 'Followed by' Compound Observation Expression

    Args:
        operands (str): compound observation operands
    """
    def __init__(self, operands):
        super(FollowedByObservationExpression, self).__init__("FOLLOWEDBY", operands)


class ParentheticalExpression(_PatternExpression):
    """Pattern Parenthetical Observation Expression

    Args:
       exp (str): observation expression
    """
    def __init__(self, exp):
        self.expression = exp
        if hasattr(exp, "root_type"):
            self.root_type = exp.root_type

    def __str__(self):
        return "(%s)" % self.expression


class _ExpressionQualifier(_PatternExpression):
    pass


class RepeatQualifier(_ExpressionQualifier):
    """Pattern Repeat Qualifier

    Args:
        times_to_repeat (int): times the qualifiers is repeated
    """
    def __init__(self, times_to_repeat):
        if isinstance(times_to_repeat, IntegerConstant):
            self.times_to_repeat = times_to_repeat
        elif isinstance(times_to_repeat, int):
            self.times_to_repeat = IntegerConstant(times_to_repeat)
        else:
            raise ValueError("%s is not a valid argument for a Repeat Qualifier" % times_to_repeat)

    def __str__(self):
        return "REPEATS %s TIMES" % self.times_to_repeat


class WithinQualifier(_ExpressionQualifier):
    """Pattern 'Within' Qualifier

    Args:
        number_of_seconds (int): seconds value for 'within' qualifier
    """
    def __init__(self, number_of_seconds):
        if isinstance(number_of_seconds, IntegerConstant):
            self.number_of_seconds = number_of_seconds
        elif isinstance(number_of_seconds, int):
            self.number_of_seconds = IntegerConstant(number_of_seconds)
        else:
            raise ValueError("%s is not a valid argument for a Within Qualifier" % number_of_seconds)

    def __str__(self):
        return "WITHIN %s SECONDS" % self.number_of_seconds


class StartStopQualifier(_ExpressionQualifier):
    """Pattern Start/Stop Qualifier

    Args:
        start_time (TimestampConstant OR datetime.date): start timestamp for qualifier
        stop_time (TimestampConstant OR datetime.date): stop timestamp for qualifier
    """
    def __init__(self, start_time, stop_time):
        if isinstance(start_time, TimestampConstant):
            self.start_time = start_time
        elif isinstance(start_time, datetime.date):
            self.start_time = TimestampConstant(start_time)
        else:
            raise ValueError("%s is not a valid argument for a Start/Stop Qualifier" % start_time)
        if isinstance(stop_time, TimestampConstant):
            self.stop_time = stop_time
        elif isinstance(stop_time, datetime.date):
            self.stop_time = TimestampConstant(stop_time)
        else:
            raise ValueError("%s is not a valid argument for a Start/Stop Qualifier" % stop_time)

    def __str__(self):
        return "START %s STOP %s" % (self.start_time, self.stop_time)


class QualifiedObservationExpression(_PatternExpression):
    """Pattern Qualified Observation Expression

    Args:
        observation_expression (PatternExpression OR _CompoundObservationExpression OR ): pattern expression
        qualifier (_ExpressionQualifier): pattern expression qualifier
    """
    def __init__(self, observation_expression, qualifier):
        self.observation_expression = observation_expression
        self.qualifier = qualifier

    def __str__(self):
        return "%s %s" % (self.observation_expression, self.qualifier)