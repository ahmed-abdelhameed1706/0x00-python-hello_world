#!/usr/bin/python3
"""
function to write in file
"""


def write_file(filename="", text=""):
    """
    function to write in file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return len(text)
