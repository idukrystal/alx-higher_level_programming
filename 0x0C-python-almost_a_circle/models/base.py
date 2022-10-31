#!/usr/bin/python3
"""
module containing base class
"""


import json


class Base:
    """base for classes for this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts arg to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves listobj to file with cls name"""
        name = cls.__name__ + '.json'
        with open(name, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                json.dump(None, f)

            for i in list_objs:
                json.dump(i.to_dictionary(), f)
