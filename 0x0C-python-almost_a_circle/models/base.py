#!/usr/bin/python3
"""
this contains the base class for the entire project
"""


import json
import os.path


class Base:
    """
    this is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        a method to convert to json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        a method to save json string to file
        """
        file_name = cls.__name__ + ".json"
        obj_dict = [i.to_dictionary() for i in list_objs if
                    list_objs is not None]

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        a method to load from json string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        a method to create an instance based on values
        """
        if cls.__name__ == "Square":
            dum = cls(1)
        else:
            dum = cls(1, 1)

        dum.update(**dictionary)

        return dum

    @classmethod
    def load_from_file(cls):
        """
        a method to load json from file
        """
        file_name = cls.__name__ + ".json"

        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, "r", encoding="utf-8") as f:
                json_str = f.read()

            json_obj = cls.from_json_string(json_str)
            obj_list = [cls.create(**json_obj[i])
                        for i in range(len(json_obj))]

        return obj_list
