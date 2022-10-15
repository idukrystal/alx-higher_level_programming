#!/usr/bin/python3
"""
0-add_integer  Module
contains function "add_integer"
example
    >>> add_integer(2, 3)
    5
"""


def add_integer(a, b=98):
    """function returns the results of adding its arguments together"""
    if (not (isinstance(a, int) or isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not (isinstance(b, int) or isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
