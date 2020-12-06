"""
:date_created: 2020-12-06
"""

import pytest

from mocking_src.data_model import Mocked


class TestMocked(object):
    """
    Test the `Mocked` utility. Instances of this class are designed to replace the original callable.
    """

    @pytest.fixture(params=[None, '', 0, 10., 10, {}, []])
    def return_value(self, request):
        """
        :type request: pytest.SubRequest
        :rtype: any
        """
        return request.param

    def test_init(self, return_value):
        """
        :type return_value: any
        """
        instance = Mocked(return_value)
        assert callable(instance)
        assert not instance.called
        assert instance.execute_args is None
        assert instance.execute_kwargs is None
        assert instance.return_value == return_value

    @pytest.mark.parametrize('args', [(), (1, 2)])
    @pytest.mark.parametrize('kwargs', [{}, {'x': 1}])
    def test_call(self, args, kwargs, return_value):
        """
        :type args: tuple
        :type kwargs: dict
        :type return_value: any
        """
        instance = Mocked(return_value)
        response = instance(*args, **kwargs)
        assert response == return_value
        assert instance.called
        assert instance.execute_args == args
        assert instance.execute_kwargs == kwargs
