#!/usr/bin/python3
"""This module contains a function that returns
True if the obj is exactly an instance of the
specified class else False"""


def is_same_class(obj, a_class) -> bool:
    """Checks if `obj` is an exact instance of `a_class`.

    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return type(obj) == a_class
