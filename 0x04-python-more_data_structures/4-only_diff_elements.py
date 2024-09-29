#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1: First set of elements.
        set_2: Second set of elements.

    Returns:
        A set containing elements that are only in one of the sets.
    """
    return set_1 ^ set_2
