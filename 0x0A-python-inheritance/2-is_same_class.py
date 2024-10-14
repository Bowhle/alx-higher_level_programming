#!/usr/bin/python3
"""This module defines a function that returns True
if the object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class."""
    if type(obj) is a_class:
        return True
    return False
