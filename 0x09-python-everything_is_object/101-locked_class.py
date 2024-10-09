#!/usr/bin/python3
"""A class that prevents the dynamic creation of attributes except for first_name."""

class LockedClass:
    """A class that allows only first_name to be dynamically created."""
    __slots__ = ["first_name"]
