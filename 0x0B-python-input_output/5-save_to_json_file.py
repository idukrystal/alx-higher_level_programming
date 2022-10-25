#!/usr/bin/python3
"""module to wrte json to a file """


def save_to_json_file(my_obj, filename):
    """saves jason rep of my_obj to filename"""
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
