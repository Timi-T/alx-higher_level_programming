#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Square:
    """
    class to represent a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing element
        """
        try:
            if size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        try:
            if type(position) is not tuple:
                raise TypeError
            if position[0] < 0:
                raise TypeError
            if position[1] < 0:
                raise TypeError
            self.__position = position
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @property
    def position(self):
        """
        Getter for position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        try:
            if value < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError:
            print("size must be an integer")
            del self.__size
        except ValueError:
            print("size must be >= 0")
            del self.__size

    @position.setter
    def position(self, value):
        """
        Setter for position
        """
        try:
            if type(value) is not tuple:
                raise TypeError
            elif value[0] < 0:
                raise TypeError
            elif value[1] < 0:
                raise TypeError
            else:
                self.__position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    @size.deleter
    def size(self):
        """
        Deleter
        """
        self.__size = None

    def area(self):
        """
        Method to get area of instance
        """
        return self.__size * self.__size

    def my_print(self):
        """
        function to print square using a hashtag
        """
        if self.__size == 0:
            print()
        for s in range(self.__size):
            for p1 in range(self.__position[0]):
                print(" ", end='')
            for s1 in range(self.__size):
                print("#", end='')
            print()
