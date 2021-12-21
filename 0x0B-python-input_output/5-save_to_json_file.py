#!/usr/bin/python3
"""
module with function to write json rep to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function to write json rep to a file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        x = json.dump(my_obj, a_file)
