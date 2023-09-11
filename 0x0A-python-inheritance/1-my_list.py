#!/usr/bin/python3
"""This module has a class MyList that inherits from
list. Has a public instance method print_sorted that
prints the list in ascending order"""


class MyList(list):
    """A custom class that inherits from `list`."""
    def print_sorted(self):
        """Prints the list item in sorted order."""
        print(sorted(self))
