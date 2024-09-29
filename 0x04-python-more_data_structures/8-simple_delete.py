#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary: The dictionary from which the key will be deleted.
        key: The key to be deleted.

    Returns:
        The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
