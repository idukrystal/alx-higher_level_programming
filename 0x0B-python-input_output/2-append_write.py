#!/usr/bin/python3
"""module apends   contents to  a file"""


def append_write(filename="", text=""):
    """apends contents of filename"""
    with open(filename, 'a', encoding="utf-8") as fil:
        written = fil.write(text)
    return written
