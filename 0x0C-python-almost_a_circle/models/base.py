#!/usr/bin/python3
"""Module that defines a Base class to manage IDs for future classes."""


class Base:
    """Base class for managing 'id' attribute for all future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """"initializes the Base class.
        Args:
            id (int): The ID of objects.
            If no id is provided, increment the class and assign it to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
