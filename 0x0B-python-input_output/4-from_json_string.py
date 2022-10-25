#!/usr/bin/python3
"""module for jason representation"""


def from_json_string(my_str):
    """return obj from json reb of my_obj"""

    import json
    return json.load(my_str)
