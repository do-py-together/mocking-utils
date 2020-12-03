"""

:date_created: 2020-12-02
"""


class DummyCls(object):
    """
    Dummy class for testing MockFunction.
    :see: TestMockFunction
    """

    def method(self):
        """
        Dummy method.
        :return: True
        """
        return True

    @classmethod
    def classmethod(cls):
        """
        Dummy classmethod.
        :return: True
        """
        return True

    @staticmethod
    def staticmethod():
        """
        Dummy staticmethod.
        :return: True
        """
        return True

    @property
    def property(self):
        """
        Dummy property
        :return: Dummy DataObject
        """
        return False
