#!/usr/bin/python3
""" importing the base class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a square that inherits from a base class Rectangle
    but also inherits a base class that also inherits another
    """
    def __init__(self, size):
        """ initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """ a class Square that inherits from Rectangle (9-rectangle.py)"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string