#!/usr/bin/python3
"""A function that writes an Object to a text file, using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be serialized to JSON.
        filename (str): The name of the file where the JSON
        representation will be written.
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(json.dumps(my_obj))