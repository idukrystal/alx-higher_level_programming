#!/usr/bin/python3
"""clases demostration task 3"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """init method for square class

        Args:
            size (int): length of sides
            position(turple(int,int): position coordinates
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (type(position) is tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""

        if not (type(position) is tuple):
            raise TypeError("position must be a tuple o\
f 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple o\
f 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints squre to stdout"""

        print("\n"*self.__position[1], end="")
        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))
        if self.__size == 0:
            print()
