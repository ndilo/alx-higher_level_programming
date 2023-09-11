#!/usr/bin/python3
"""
Module contains class with public instance
and raises exception when required
"""


class BaseGeometry:
    """
    class Base has public instance
    """
    def area(self):
        """
        function that raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
