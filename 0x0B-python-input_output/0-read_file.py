#!/usr/bin/python3
"""module output content of a file"""


def read_file(filename=""):
    """outputs xontents of filename"""
    with open(filename, 'r', encoding='utf-8') as file:
        read_data = file.read()
    print(read_data)
