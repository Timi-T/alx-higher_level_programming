#!/usr/bin/python3
"""
Module containing function to add 2 integers
"""


def add_integer(a, b=98):
    """
    function to add 2 integers
    """
    j = 5
    k = 5.078
    try:
        if type(a) == type(k):
            a = int(a)
        if type(b) == type(k):
            b = int(b)
        if type(a) != type(j):
            var = 'a'
            raise TypeError
        if type(b) != type(j):
            var = 'b'
            raise TypeError
    except TypeError:
        print("{} must be an integer".format(var))
    else:
        return a + b
