#!/usr/bin/python3
"""module output content of a file"""


def read_file(filename=""):
    """outputs contents of filename"""
    with open(filename, 'r', encoding="utf-8") as fil:
        read_data = fil.read()
        print(read_data)
