#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        side_length (int): The length of a side of the square.
    """

    def __init__(self, side_length=0):
        """
        Initializes a Square instance.

        Args:
            side_length (int): The length of a side of the square. Defaults to 0.
        """
        self.side_length = side_length

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (side_length squared).
        """
        return self.side_length ** 2