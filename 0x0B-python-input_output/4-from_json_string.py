#!/usr/bin/python3
"""
module with function  to convert json to string
"""


import json


def from_json_string(my_str):
    """
    function to convert json to string
    """
    return json.loads(my_str)
