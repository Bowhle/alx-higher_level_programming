#!/usr/bin/python3
""" the class Rectangle that inherits from Base"""
from models.base import Base
""" this is importing the base object defined in model dir in file base.py"""


class Rectangle(Base):
    """ THe class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ the with getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ the width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ the setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ The area of a Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        [print("") for y in range(self.__y)]
        for length in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width, end='')
            print()

    def __str__(self):
        """ it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        class_id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return (f"[Rectangle] ({class_id}) {x}/{y} - {width}/{height}")

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute: """
        argument = []
        for item in args:
            argument.append(item)
        if len(argument) >= 1:
            self.id = argument[0]
        if len(argument) >= 2:
            self.width = argument[1]
        if len(argument) >= 3:
            self.height = argument[2]
        if len(argument) >= 4:
            self.x = argument[3]
        if len(argument) >= 5:
            self.y = argument[4]

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {"x": getattr(self, "x"),
                "y": getattr(self, "y"),
                "id": getattr(self, "id"),
                "height": getattr(self, "height"),
                "width": getattr(self, "width")
                }
