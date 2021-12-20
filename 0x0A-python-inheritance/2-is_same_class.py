#!/usr/bin/python3
"""
module with function to check for instance
"""


def is_same_class(obj, a_class):
    """
    function to check if an object is an instance of a class
    """
    if a_class != object:
        return isinstance(obj, a_class)
