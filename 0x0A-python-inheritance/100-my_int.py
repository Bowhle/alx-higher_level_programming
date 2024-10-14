#!/usr/bin/python3
""" A class MyInt that inherits from int """


class MyInt(int):
    """ A class that inherits from int """

    def __eq__(self, value):
        """ Invert the equality operator """
        return super().__ne__(value)  # Use the base class's not equal

    def __ne__(self, value):
        """ Invert the inequality operator """
        return super().__eq__(value)  # Use the base class's equal

    def __str__(self):
        """ Return the string representation of the integer """
        return super().__str__()
