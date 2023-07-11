#!/usr/bin/python3
"""
function to dump data to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    dumps data to file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
