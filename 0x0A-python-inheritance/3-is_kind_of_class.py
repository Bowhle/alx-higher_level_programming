#!/usr/bin/python3
""" A function that return True if obj is an inheritance"""


def is_kind_of_class(obj, a_class):
    """ This is a kind of class that checks if an obj is from a class """
    if isinstance(obj, a_class):
        return True
    return False