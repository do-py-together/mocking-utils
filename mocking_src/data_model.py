"""

:date_created: 2020-12-02
"""


class Mocked(object):
    """
    The mocked function. When the function is called, the args and kwargs are captured.
    NOTE: This has been used and created a few times now, this should be the real one. Import from here.
    """
    called = False
    execute_args = None
    execute_kwargs = None

    def __init__(self, return_value):
        """
        :param return_value: The value that will be return when called.
        """
        self.return_value = return_value

    def __call__(self, *args, **kwargs):
        """
        Capture execution args and kwargs, and set the called flag to true.
        :param args: Execution args that will be captured in the instance.
        :param kwargs: Execution kwargs that will be captured in the instance.
        """
        self.called = True
        self.execute_args = args
        self.execute_kwargs = kwargs
        return self.return_value
