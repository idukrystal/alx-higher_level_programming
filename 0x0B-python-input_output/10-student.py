#!/usr/bin/python3
""" Studentclass module
"""


class Student:
    """ Student Class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = self.__dict__
        if isinstance(attrs, list) & all(isinstance(it, str) for it in attrs):
            for key in dic:
                if key not in attrs:
                    del dic[key]
        return dic
