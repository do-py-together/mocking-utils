"""
:date_created: 2020-01-14
"""

import pytest

from dummy import DummyCls
from mocking_utils.mock_function import MockFunction


class TestMockFunction(object):
    """
    Test the MockFunction testing util.
    As of today, 2019-01-14, static methods are neither supported or tested.
    """

    @pytest.fixture(autouse=True)
    def validate(self):
        """
        After each test runs assert that the mock was reset correctly.
        """

        def _validate_all():
            assert DummyCls().method() is True
            assert DummyCls.classmethod() is True

        _validate_all()
        yield
        _validate_all()

    @pytest.mark.parametrize('obj', [
        pytest.param(DummyCls),
        pytest.param(None, marks=pytest.mark.xfail),
        pytest.param('string', marks=pytest.mark.xfail),
        pytest.param(bool, marks=pytest.mark.xfail),
        pytest.param(type, marks=pytest.mark.xfail),
        pytest.param(1, marks=pytest.mark.xfail),
        pytest.param(True, marks=pytest.mark.xfail),
        ])
    @pytest.mark.parametrize('fn_name', [
        'method',
        'classmethod',
        # 'staticmethod',
        pytest.param('not_a_method', marks=pytest.mark.xfail),
        pytest.param(None, marks=pytest.mark.xfail),
        ])
    def test_invalid_mock(self, obj, fn_name):
        """
        :param obj: The object reference containing the fn_name to mock.
        :type fn_name: str or types.NoneType
        """
        mock = MockFunction(obj, fn_name, False)
        mock.reset()

    @pytest.mark.parametrize('obj, fn_name', [
        (DummyCls(), 'method'),
        (DummyCls, 'classmethod'),
        # (DummyCls, 'staticmethod'),
        ])
    def test_mock(self, obj, fn_name):
        """
        :param obj: instance or class reference for assertion.
        :type fn_name: str
        """
        mock = MockFunction(DummyCls, fn_name, False)
        assert getattr(obj, fn_name)() is False
        mock.reset()

    @pytest.mark.parametrize('obj, fn_name', [
        (DummyCls(), 'method'),
        (DummyCls, 'classmethod'),
        # (DummyCls, 'staticmethod'),
        ])
    def test_mock_call(self, obj, fn_name):
        """
        :param obj: instance or class reference for assertion.
        :type fn_name: str
        """
        def _noop(*args, **kwargs):
            """ No operation """
            return False

        mock = MockFunction(DummyCls, fn_name, _noop, call=True)
        assert getattr(obj, fn_name)() is False
        mock.reset()

    @pytest.mark.parametrize('obj, fn_name', [
        (DummyCls(), 'method'),
        (DummyCls, 'classmethod'),
        # (DummyCls, 'staticmethod'),
        ])
    def test_mock_reset(self, obj, fn_name):
        """
        :param obj: instance or class reference for assertion.
        :type fn_name: str
        """
        mock = MockFunction(DummyCls, fn_name, False)
        assert getattr(obj, fn_name)() is False
        mock.reset()
        assert getattr(obj, fn_name)() is True
