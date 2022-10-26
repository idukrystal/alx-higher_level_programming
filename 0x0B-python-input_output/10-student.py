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
        if (
                (isinstance(attrs, list) and
                 all(isinstance(it, str)
                     for it in attr)
                 )
        ):
            att = [key for key in dic if key not in attrs]
            for key in att:
                del dic[key]
        return dic
