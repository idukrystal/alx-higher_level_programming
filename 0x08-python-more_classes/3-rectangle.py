#!/usr/bin/python3

""""a sample module for a Rectangle class"""


class Rectangle:
    """a Rectangle object"""
    @property
    def width(self):
        return self.__width__

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        return self.__height__

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def area(self):
        return self.width * self.height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        line = '#'*self.width
        return ((line + '\n') * (self.height - 1)) + line
