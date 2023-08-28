#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as k:
        stderr.write("Exception: {}\n".format(k))
        return (None)
