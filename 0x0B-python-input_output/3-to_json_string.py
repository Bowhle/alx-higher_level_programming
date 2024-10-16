#!/usr/bin/python3
"""A function that returns the JSON representation of an object."""

import json  # This will enable us to use the json module


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
