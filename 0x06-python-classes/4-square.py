#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Square:
    """
    class to represent a square
    """

    def __init__(self, size=0):
        pass
        """
        Iinitializing element
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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
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
    @size.deleter
    def size(self):
        self.__size = None
    def area(self):
        return self.__size * self.__size
