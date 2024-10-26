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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

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

    def update(self, *args, **kwargs):
        """Update the Square attributes.

        Args:
            *args: Non-keyworded arguments to update attributes.
                1st argument: id
                2nd argument: size
                3rd argument: x
                4th argument: y
            **kwargs: Keyworded arguments to update attributes.
        """
        if args and len(args) > 0:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
