"""
:date_created: 2020-12-06
"""
import pytest

from mocking_src.utils import powerset, powerset_concat


@pytest.mark.parametrize('iterable, empty_is_valid, expected_output', [
    ([1, 2, 3], True, [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]),
    ([1, 2, 3], False, [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]),
    ])
def test_powerset(iterable, empty_is_valid, expected_output):
    """
    :type iterable: list
    :type empty_is_valid: bool
    :type expected_output: list of tuple
    """
    assert list(powerset(iterable, empty_is_valid=empty_is_valid)) == expected_output


@pytest.mark.parametrize('iterable, empty_is_valid, expected_output', [
    (['a', 'b', 'c'], True, ['', 'a', 'b', 'c', 'a,b', 'a,c', 'b,c', 'a,b,c']),
    (['a', 'b', 'c'], False, ['a', 'b', 'c', 'a,b', 'a,c', 'b,c', 'a,b,c']),
    pytest.param([1, 2, 3], False, [], marks=pytest.mark.xfail(raises=TypeError))
    ])
def test_powerset_concat(iterable, empty_is_valid, expected_output):
    """
    :type iterable: list of str
    :type empty_is_valid: bool
    :type expected_output: list of str
    """
    assert list(powerset_concat(iterable, empty_is_valid=empty_is_valid)) == expected_output
