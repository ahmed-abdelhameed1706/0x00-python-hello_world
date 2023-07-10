#!/usr/bin/python3
"""
a function that returns true if obj is instance of a class
"""


def is_same_class(obj, a_class):
    """
    returns true or false
    obj is a an object to check
    a_class is a class to compare the obj to
    """
    if type(obj) is a_class:
        return True
    else:
        return False
