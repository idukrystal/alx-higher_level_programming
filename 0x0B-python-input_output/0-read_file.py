#!/usr/bin/python3
"""module output content of a file"""


def read_file(filename=""):
    """outputs xontents of filename"""
    with open(filename, 'r', 'utf-8') as file:
        read_data = read(file)
    print(read_data)
