#!/usr/bin/python3
"""A class that defines BaseGeometry."""


class BaseGeometry:
    """A class that serves as a base for geometry-related classes."""

    def area(self):
        """Raises an Exception because the area is not implemented."""
        raise Exception("area() is not implemented")
