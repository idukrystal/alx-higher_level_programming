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

    @property
    def size(self):
        """Getter for size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        args:
            value(int): new size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints squre to stdout"""

        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()