#!/usr/bin/python3
"""
function to return an object from json string
"""


import json


def from_json_string(my_str):
    """
    returns an object from str
    """
    return json.loads(my_str)
