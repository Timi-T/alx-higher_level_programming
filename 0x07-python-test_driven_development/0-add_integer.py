#!/usr/bin/python3
"""
Module containing function to add 2 integers
"""


def add_integer(a, b=98):
    """
    function to add 2 integers
    """
    if isinstance(a, float) is True:
        a = int(a)
    if isinstance(b, float) is True:
        b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    else:
        return a + b
