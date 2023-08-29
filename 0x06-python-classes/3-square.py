#!/usr/bin/python3
"""
Class that defines a square based on 2-square.py
"""


class Square:
    """
    Private instance attribute size
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= )")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return (self.__size ** 2)
