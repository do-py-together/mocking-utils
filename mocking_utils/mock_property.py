"""

:date_created: 2020-12-02
"""


class MockProperty(object):
    """
    Mock the property of a class.
    """

    def __init__(self, obj, property_name, response):
        """
        :param obj: The object which contains the object that will be replaced.
        :type obj: object (module, object, etc)
        :param property_name: Name of the property in the object that will be replaced.
        :type property_name: str
        :param response: the mocked property value
        """
        assert hasattr(obj, property_name), '%s has no property "%s"' % (obj, property_name)
        self.obj = obj
        self.property_name = property_name
        self.response = response
        # Cache old property and set function as this instance.
        self.cached_property = getattr(self.obj, self.property_name)
        setattr(self.obj, self.property_name, self.response)

    def reset(self):
        """
        Replace the mocked property in the object, with the original. This should set it
        back to it's original state. It is VERY IMPORTANT that we call this method to cleanup,
        otherwise we may see unintended side effects.
        """
        setattr(self.obj, self.property_name, self.cached_property)
