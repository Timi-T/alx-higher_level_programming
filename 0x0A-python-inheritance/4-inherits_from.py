#!/usr/bin/python3
"""
module with function to chech if object inherits from class or superclass
"""


def inherits_from(obj, a_class):
    """
    function to check if object inherits from class or superclass
    """
    if issubclass(a_class, type(obj)) == False:
        return True
    else:
        return False
