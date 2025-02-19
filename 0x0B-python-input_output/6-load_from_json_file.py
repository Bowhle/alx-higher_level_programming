#!/usr/bin/python3
"""A function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object deserialized from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
