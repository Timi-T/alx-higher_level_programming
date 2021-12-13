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
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is False:
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
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        function to return area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        function to return rectangle perimeter
        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        function to represent a squre with #
        """
        for h in range(self.__height):
            for w in range(self.__width):
                print('#', end='')
            if h != self.__height - 1:
                print()
        return ''
