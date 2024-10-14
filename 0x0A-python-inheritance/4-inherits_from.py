#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a class that inherited from a_class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
