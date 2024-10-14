#!/usr/bin/python3
"""A new class based on 6-base_geometry.py."""

# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate the width and assign it to a private attribute
        self.integer_validator("width", width)
        self.__width = width

        # Validate the height and assign it to a private attribute
        self.integer_validator("height", height)
        self.__height = height
