#!/usr/bin/python3
"""
module with empty class
"""


class BaseGeometry():
    """
    geometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
