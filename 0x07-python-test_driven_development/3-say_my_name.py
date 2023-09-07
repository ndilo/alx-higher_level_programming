#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    """ Check if first_name and last_name are strings """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    """ Print the message """
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
