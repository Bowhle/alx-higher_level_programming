#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Representing a square object with a private size"""

    def __init__(self, size=0):
        """
        Initialise the square with a size
        Raises TypeError: if size is not an int
        Raises ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0
            raise ValueError("size must be >=0")

        self.__size = size
