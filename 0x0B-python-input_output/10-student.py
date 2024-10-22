#!/usr/bin/python3
"""A class that defines a student."""


class Student:
    """A Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
