#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.

    Args:
        a_dictionary: A dictionary where keys are strings
                      and values are integers.

    Returns:
        The key with the highest value, or None if no score is found.
    """
    if not a_dictionary:
        return None

    # Initialize variables to track the best key and its score
    best_key = None
    max_score = float('-inf')  # Start with the smallest possible integer

    # Iterate through the dictionary
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
