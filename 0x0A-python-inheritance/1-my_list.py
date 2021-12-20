#!/usr/bin/python3
"""
module with class mylist
"""


class MyList(list):
    """
    class to inherit from list
    """
    def print_sorted(self):
        a = sorted(self)
        print(a)
        return self
