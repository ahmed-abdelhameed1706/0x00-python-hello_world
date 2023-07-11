#!/usr/bin/python3
"""
a student class
"""


class Student:
    """
    a class that reprents a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            jdict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    jdict[key] = value
            return jdict
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
