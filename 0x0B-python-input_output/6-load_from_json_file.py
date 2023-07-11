#!/usr/bin/python3
"""
loads a json file into a variable
"""


import json


def load_from_json_file(filename):
    """
    loads a json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json_file = json.load(f)
