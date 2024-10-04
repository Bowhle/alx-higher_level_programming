#!/usr/bin/python3
"""Representing a square"""


class Square():
    """A square object representation"""

    def __init__(self, size=0):
        """ initialize the newly created square
        where: size equates the size of the square and given a default value 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
