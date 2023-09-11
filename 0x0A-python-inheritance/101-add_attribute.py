#!/usr/bin/python3
"""
Module has a function that adds new
attributes to an object
"""


def add_attribute(ob, attr, value):
    """
    add attribute to class, else
    Raise:
        error
    """
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
