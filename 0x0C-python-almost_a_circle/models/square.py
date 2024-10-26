#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, custom_id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            custom_id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, custom_id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The new size of the square (width and height).
        """
        self.width = value
        self.height = value
