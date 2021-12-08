#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Square:
    """
    class to represent a square
    """

    def __init__(self, size=0):
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
            del square.self
        except ValueError:
            print("size must be >= 0")
            del square.self
