"""

:date_created: 2020-12-02
"""

from mocking_utils.utils import is_classmethod


class MockFunction(object):
    """
    Mock the function of a class, module, or any object really. This is very useful when unit testing,
    because it can avoid calls to external resources and keep the test contained. It allows you to
    specify the return value of the "mock function" so that the code flows as expected/designed.
    NOTE: It is VERY IMPORTANT that we call "reset" to cleanup, otherwise we may see unintended side effects.
    """
    called = False
    call_args = None
    call_kwargs = None

    def __init__(self, obj, fn_name, response, call=False):
        """
        Set the function of an object to this instance so that when another section of code calls the function,
        this instances's __call__ is executed instead.
        NOTE: It is VERY IMPORTANT that we call "reset" to cleanup, otherwise we may see unintended side effects.

        NOTE: static methods are NOT supported as of 2019-12-17
        :param obj: The object which contains the object that will be replaced.
        :type obj: object (module, object, etc)
        :param fn_name: Name of the function in the object that will be replaced.
        :type fn_name: str
        :param call: Tell the __call__ method to execute the mock response as a callable.
        :type call: bool
        :param response: the mocked return value
        """
        assert hasattr(obj, fn_name), '%s has no attribute "%s"' % (obj, fn_name)
        self.obj = obj
        self.fn_name = fn_name
        self.response = response
        self.call = call
        # Cache old function and set function as this instance.
        self.cached_fn = getattr(self.obj, self.fn_name)
        self.is_classmethod = is_classmethod(obj, self.cached_fn)
        if call:
            assert callable(self.response), 'Invalid mock callable.'
            # Check if it is a class method, so we can attach the mock fn correctly.
            if self.is_classmethod:
                setattr(self.obj, self.fn_name, classmethod(self))
            else:
                setattr(self.obj, self.fn_name, self)
        else:
            setattr(self.obj, self.fn_name, self)

    def reset(self):
        """
        Replace the mocked function in the object, with the original. This should set it
        back to it's original state. It is VERY IMPORTANT that we call this method to cleanup,
        otherwise we may see unintended side effects.
        """
        setattr(self.obj, self.fn_name, self.cached_fn)

    def __call__(self, *args, **kwargs):
        """
        This is the "mock function" that is called. All we do here is return the response value defined in __init__.
        :param args: ignored
        :param kwargs: ignored
        :return: the response as defined in __init__
        """
        self.called = True
        self.call_args = args
        self.call_kwargs = kwargs
        if self.call:
            assert callable(self.response), 'Invalid mock callable.'
            return self.response(*args, **kwargs)
        else:
            return self.response
