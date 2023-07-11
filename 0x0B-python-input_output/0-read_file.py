#!/usr/bin/python3
"""
a function that reads a text from a file
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read())
