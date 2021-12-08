#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Square:
    """
    A class to rep a square
    """

    def __init__(self, size):
        """
        Initialization of a square
        """
        self.__size = size
