#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiplies all values in a dictionary by 2.

    Args:
        a_dictionary: The dictionary whose values will be multiplied.

    Returns:
        A new dictionary with all values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
