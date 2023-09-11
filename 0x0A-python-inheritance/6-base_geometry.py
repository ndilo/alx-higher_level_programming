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
