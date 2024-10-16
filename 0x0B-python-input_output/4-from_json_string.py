#!/usr/bin/python3
"""A function that returns an object
(Python data structure) from a JSON string.
"""
import json
"""Using the json module as we will be converting 
the JSON string to a Python data structure.
"""


def from_json_string(my_str):
    """Convert a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
