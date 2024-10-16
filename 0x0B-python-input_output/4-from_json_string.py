#!/usr/bin/python3
""" a function that returns an object (Python data structure)"""
import json
""" using the json module as are converting the json file to py"""


def from_json_string(my_str):
    """ the function that collects a json str and return a py data struct """
    return json.loads(my_str)