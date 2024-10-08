#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to be updated.
        key: The key to be replaced or added.
        value: The value associated with the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
