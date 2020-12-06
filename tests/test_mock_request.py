"""
:date_created: 2020-12-06
"""

import pytest

from mocking_src.mock_request import MockRequest, MockRequestHtml


class TestMockRequest(object):

    @pytest.mark.parametrize('status_code', [200, 201, 403, 404, 500])
    @pytest.mark.parametrize('data', [None, {}, {'x': 1}])
    def test_init(self, status_code, data):
        """
        :type status_code: int
        :type data: any
        """
        inst = MockRequest(status_code, data)
        assert inst.status_code == status_code
        assert inst.data == data
        assert inst.json() == data

    @pytest.mark.parametrize('args', [(), (1, 2)])
    @pytest.mark.parametrize('kwargs', [{}, {'x': 1}])
    @pytest.mark.parametrize('data', [None, {}, {'y': 1}])
    def test_call(self, args, kwargs, data):
        """
        :type args: tuple
        :type kwargs: dict
        :type data: any
        """
        inst = MockRequest(200, data)
        resp = inst(*args, **kwargs)
        assert inst.request_args == args
        assert inst.request_kwargs == kwargs
        assert resp.json() == data


class TestMockRequestHtml(object):

    @pytest.mark.parametrize('status_code', [200, 201, 403, 404, 500])
    @pytest.mark.parametrize('html', ['hello world'])
    def test_init(self, status_code, html):
        """
        :type status_code: int
        :type html: str
        """
        inst = MockRequestHtml(status_code, html)
        assert inst.status_code == status_code
        assert inst.html == html
        assert inst.text == html
