#!/usr/bin/python3
"""Representing a square."""


class Square:
    """A square object representation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the newly created square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter method for size
        self.position = position  # Use the setter method for position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public method: computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Alternatively: return self.__size * self.__size

    def my_print(self):
        """
        Public method: prints the square with the character #.

        If size is 0, prints an empty line. Position is used for spacing.
        """
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print the empty lines for vertical position
        for _ in range(self.__position[1]):
            print()

        # Print the square with the specified position
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
