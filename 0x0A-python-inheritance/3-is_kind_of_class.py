#!/usr/bin/python3
"""
a function to check if the obj is instance or subclass of a class
"""


def is_kind_of_class(obj, a_class):
    """
    a function to check
    obj is an object
    a class is a class to compare to
    return true or false
    """
    if isinstance(obj, a_class) or issubclass(obj.__class__, a_class):
        return True
    else:
        return False
