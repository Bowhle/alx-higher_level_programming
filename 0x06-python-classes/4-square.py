#!/usr/bin/python3
"""Representing a square."""


class Square:
    """A square object representation."""

    def __init__(self, size=0):
        """Initialize the newly created square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square
        return:
        int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method: computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
