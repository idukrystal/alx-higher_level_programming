#!/usr/bin/python3
"a module that has functions to print a square"


def print_square(size):
    "function to print square"

    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise ValueError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(('#'*size))
