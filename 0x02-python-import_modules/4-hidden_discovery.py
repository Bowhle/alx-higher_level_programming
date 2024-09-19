#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all attributes of the module
    attributes = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in attributes if not name.startswith('__')]

    # Sort the names alphabetically
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
