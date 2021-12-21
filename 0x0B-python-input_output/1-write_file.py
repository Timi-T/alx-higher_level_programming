#!/usr/bin/python3
"""
module with function to write to a file
"""


def write_file(filename="", text=""):
    """
    function to write to a file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        no_of_bytes = a_file.write(text)
    return no_of_bytes
