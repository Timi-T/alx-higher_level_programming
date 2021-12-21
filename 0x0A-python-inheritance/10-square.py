#!/usr/bin/python3
"""
module with square class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """
    square class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __repr__(self):
        print("[{}] {:d}/{:d}".format(self.__class__.__name__,
                                      self.__size, self.__size))

    def __str__(self):
        return ("[{}] {:d}/{:d}".format(self.__class__.__name__,
                                        self.__size, self.__size))
