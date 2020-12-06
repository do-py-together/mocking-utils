"""
Testing utilities & helpers.
:date_created: 2019-12-17
"""
import inspect
from itertools import chain, combinations


def powerset(iterable, empty_is_valid=True):
    """
    :type iterable: list
    :type empty_is_valid: bool
    :rtype: collections.Iterable[tuple]
    """
    s = iterable
    return (x for x in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)) if x or empty_is_valid)


def powerset_concat(iterable, empty_is_valid=True):
    """
    This utility func creates a powerset of the elements provided in iterable via string-concats.
    :type iterable: list of str
    :type empty_is_valid: bool
    :rtype: list of str
    """
    return (','.join(d) for d in powerset(iterable, empty_is_valid=empty_is_valid))


def is_classmethod(cls, method):
    """
    Check if a method is a classmethod. Supports Python 2/3.
    :ref: https://stackoverflow.com/questions/19227724/check-if-a-function-uses-classmethod
    :param cls: Class
    :type cls: type
    :param method: Name of the method to check
    :type method: callable
    :rtype: bool
    """
    return inspect.ismethod(method) and hasattr(method, '__self__') and getattr(method, '__self__') is cls
