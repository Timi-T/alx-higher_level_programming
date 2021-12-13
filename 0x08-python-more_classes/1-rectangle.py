#!/usr/bin/python3
"""
module for defining a rectangle
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        initialization of instance
        """
        if type(width) != type(1):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != type(1):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height musts be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) != type(1):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if type(value) != type(1):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
