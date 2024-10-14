#!/usr/bin/python3
"""A function that returns True if obj is an instance of a_class
or an instance of a class that inherited from a_class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or inherited from it.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a_class or its subclasses;
        otherwise, False.
    """
    return isinstance(obj, a_class)
