#!/usr/bin/python3
"""
this contains the base class for the entire project
"""


class Base:
    """
    this is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
