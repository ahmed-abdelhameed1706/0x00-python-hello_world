#!/usr/bin/python3
"""
a function to return true of obj class is subclass of supre class
"""


def inherits_from(obj, a_class):
    """
    obj is an object
    a_class is a class to check
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
