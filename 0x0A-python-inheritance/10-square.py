#!/usr/bin/python3
"""Importing the Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from the Rectangle class."""

    def __init__(self, size):
        """Initialization of the square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)  # Validate the size
        self.__size = size  # Private attribute for size
        super().__init__(size, size)  # Initialize the parent class

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size  # Area formula: size^2

    def __str__(self):
        """String representation of the square.

        Returns:
            str: Description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
