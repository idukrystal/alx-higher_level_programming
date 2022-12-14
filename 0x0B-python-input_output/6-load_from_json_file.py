#!/usr/bin/python3
"""module to loads json from  a file """


def load_from_json_file(filename):
    """load jason obj ftom filename"""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
