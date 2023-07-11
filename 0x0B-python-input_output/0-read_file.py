#!/usr/bin/python3
"""
a function that reads a text from a file
"""


def read_file(filename=""):
    """
    function that reads a text from a file
    filename is the filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
