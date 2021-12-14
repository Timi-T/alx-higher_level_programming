#!/usr/bin/python3
"""
say my name module
"""


def say_my_name(first_name, last_name=""):
    """
    function to say my name
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
