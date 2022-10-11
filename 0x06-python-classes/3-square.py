#!/usr/bin/python3
"""clases demostration task 3"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """init method for square class

        Args:
            size (int): length of sides
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of square"""

        return self.__size * self.__size
