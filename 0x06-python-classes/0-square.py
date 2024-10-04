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
        """
        self.side_length = side_length
