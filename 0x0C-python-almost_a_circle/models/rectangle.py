#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base and manages
    width, height, x, and y.
    """

    def __init__(self, width, height, x=0, y=0, custom_id=None):
        """Initializes the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle.
            y (int): The y position of the rectangle.
            custom_id (int): The ID of the instance.
        """
        super().__init__(custom_id)
        self.width = width  # Triggers width setter
        self.height = height  # Triggers height setter
        self.x = x  # Triggers x setter
        self.y = y  # Triggers y setter

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle instance using the '#' character"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a str rep of a Rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args):
        """Assigns args to attributes based on their order"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate with validation."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate with validation."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
