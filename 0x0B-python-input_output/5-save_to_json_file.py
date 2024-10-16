#!/usr/bin/python3
"""A function that writes an Object to a text file, using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be serialized to JSON.
        filename (str): The name of the file where the JSON representation
                        will be written.
    """
    # Convert set to list if my_obj is a set
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)  # Directly dump the JSON object to the file.
