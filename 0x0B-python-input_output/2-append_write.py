#!/usr/bin/python3
"""
function to append to file
"""


def write_file(filename="", text=""):
    """
    function to append to file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    return len(text)
