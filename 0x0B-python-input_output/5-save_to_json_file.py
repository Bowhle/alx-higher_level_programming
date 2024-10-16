#!/usr/bin/python3
""" writes an Object to a text file, using a JSON"""
import json
""" this module will be used as json is needed"""


def save_to_json_file(my_obj, filename):
    """ a function that writes a to a text file"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(json.dumps(my_obj))
