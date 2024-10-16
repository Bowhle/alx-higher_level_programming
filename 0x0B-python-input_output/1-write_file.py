#!/usr/bin/python3
"""A function that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8).

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
