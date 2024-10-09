#!/usr/bin/python3
"""A function that computes the addition of two integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to int and return the sum
    return int(a) + int(b)
