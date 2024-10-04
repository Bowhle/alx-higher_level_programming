#!/usr/bin/python3
"""Module that defines a MagicClass."""

import math


class MagicClass:
    """A class that defines a circle with methods to calculate area and circumference."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance. """
        self.__radius = 0  # Set default radius

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius  # Set the radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
