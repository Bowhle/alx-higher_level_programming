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

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square.

        Args:
            *args: A list of positional arguments to assign to attributes.
                1st argument -> id
                2nd argument -> size
                3rd argument -> x
                4th argument -> y
            **kwargs: A dictionary of key-value pairs to assign to attributes
                      if *args is not provided.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
