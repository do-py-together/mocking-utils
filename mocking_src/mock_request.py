"""

:date_created: 2020-12-02
"""


class MockRequest(object):
    """
    Mock a request with a response data and a status code.
    """
    request_args = None
    request_kwargs = None

    def __init__(self, status_code, data):
        """
        Initializes the function and sets the variables.
        :param status_code: This is the expected status code of the request.
        :param data: This is the data that is passed in upon creation of the object. Used as data for the Request.
        """
        self.status_code = status_code
        self.data = data

    def __call__(self, *args, **kwargs):
        """
        An instance of this class may be used to mock a request with `call` set to True. This will
        cache the args and kwargs used for making the request.
        :rtype: MockRequest
        """
        self.request_args = args
        self.request_kwargs = kwargs
        return self

    def json(self, *args, **kwargs):
        """
        Returns the data that was passed into the Request. Similar to the Request.json() function.
        :param args: ignored
        :param kwargs: ignored
        :rtype: str
        """
        return self.data


class MockRequestHtml(object):
    """
    Mock a request with a response data and a status code.
    """

    def __init__(self, status_code, html):
        """
        Initializes the function and sets the variables.
        :param status_code: This is the expected status code of the request.
        :param html: Html page.
        """
        self.status_code = status_code
        self.html = html

    @property
    def text(self, *args, **kwargs):
        """
        Returns the data that was passed into the Request. Similar to the Request.json() function.
        :param args: ignored
        :param kwargs: ignored
        :rtype: str
        """
        return self.html
