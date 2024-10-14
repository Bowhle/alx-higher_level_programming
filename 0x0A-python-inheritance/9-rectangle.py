#!/usr/bin/python3
"""A Rectangle class that inherits from BaseGeometry."""

# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: Description of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
