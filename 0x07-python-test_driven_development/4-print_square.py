#!/usr/bin/python3
"""
module for function to print square
"""


def print_square(size):
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for s in range(size):
            for q in range(size):
                print('#', end='')
            print()
