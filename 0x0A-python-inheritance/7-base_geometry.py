#!/usr/bin/python3
"""A class that defines BaseGeometry."""


class BaseGeometry:
    """A class that serves as a base for geometry-related classes."""

    def area(self):
        """Raises an Exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value to ensure it is a positive integer.

        Args:
            name: A string representing the name of the variable.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
