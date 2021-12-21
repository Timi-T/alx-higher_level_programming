#!/usr/bin/python3
"""
module with function to append to a file
"""


def append_write(filename="", text=""):
    """
    function to append a string to a file
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        no_of_append = a_file.write(text)
    return no_of_append
