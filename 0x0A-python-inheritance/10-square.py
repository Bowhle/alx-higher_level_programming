#!/usr/bin/python3
"""A Square class that inherits from Rectangle."""

# Import the Rectangle class from the 8-rectangle module
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Instantiation with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call the parent constructor

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: Description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
