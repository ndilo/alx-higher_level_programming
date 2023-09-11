#!/usr/bin/python3
"""This module contains a function that returns True
if the object is an instance of, or if the object
is an instance of a class that inherited from, the
specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance of `a_class` or `object`.

    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return isinstance(obj, a_class)
