"""

:date_created: 2020-12-02
"""

from mocking_src.mock_property import MockProperty
from testing.dummy import DummyCls


class TestMockProperty(object):
    """
    Test the MockProperty testing util.
    """

    def test_mock_property(self):
        """
        Test creation, resetting, and that the property was reset correctly.
        """
        original = DummyCls().property
        mocked = 1024
        assert original != mocked
        mock = MockProperty(DummyCls, 'property', mocked)
        assert DummyCls().property == mocked
        mock.reset()
        assert DummyCls().property == original
