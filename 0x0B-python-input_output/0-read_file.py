#!/usr/bin/python3
"""
module with function to read files
"""


def read_file(filename=""):
    """
    function to read a file
    """
    with open(filename, encoding='utf-8') as a_file:
        file_content = a_file.read()
    print(file_content, end='')
