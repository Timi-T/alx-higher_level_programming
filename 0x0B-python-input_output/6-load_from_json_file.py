#!/usr/bin/python3
"""
module with function to decode json to object
"""


import json


def load_from_json_file(filename):
    """
    function to decode json to object
    """
    with open(filename, mode='r+', encoding='utf-8') as a_file:
        return json.load(a_file)
