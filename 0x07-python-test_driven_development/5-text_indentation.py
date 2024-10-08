#!/usr/bin/python3
"""A function that prints a text with 2 new lines after certain characters."""


def text_indentation(text):
    """Prints text with two new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0

    # Loop through the text
    while c < len(text):
        print(text[c], end="")  # Print the current character

        # Check if the character is one of the specified punctuation marks
        if text[c] in ".?:":
            print("\n")  # Print an additional new line
            print()  # Print another new line

            # Move to the next character that is not a space
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue

        c += 1  # Move to the next character
