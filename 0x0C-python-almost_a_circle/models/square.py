#!/usr/bin/python3
"""
module containing square class
"""


Base = __import__("base").Base
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str repr"""
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.width
                )

    def to_dictionary(self):
        """returns dict repr of object"""
        return vars(self)

    @property
    def size(self):
        """returns width or height"""
        return self.width
    @size.setter
    def size(self, size):
        """sets width and height"""
        self.width = size
        self.height = size
a = Square(9,5,5,5)
print(a.to_dictionary())
