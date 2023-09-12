#!/usr/bin/python3
"""Student Module"""


class Student:
    """Defines a Student class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance."""
        if isinstance(attrs, list) and \
                (all(isinstance(s, str) for s in attrs)):
            return {l: value for l, value in dict(self.__dict__).items() if l in attrs}

        return self.__dict__
