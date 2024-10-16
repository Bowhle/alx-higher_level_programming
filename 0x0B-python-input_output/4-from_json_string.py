#!/usr/bin/python3
"""A function that returns an object(Python data structure) from a JSON string."""
import json
"""Using the json module as we will be converting the JSON string to a Py data structure."""


def from_json_string(my_str):
    """This function collects a json string and gives it a python data structure"""
    return json.loads(my_str)
