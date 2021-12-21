#!/usr/bin/python3
"""
module with function to convert to json representation
"""


import json


def to_json_string(my_obj):
    """
    function to convert to json representation
    """
    return json.dumps(my_obj)
