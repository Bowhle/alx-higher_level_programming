#!/usr/bin/python3
"""A function that returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
