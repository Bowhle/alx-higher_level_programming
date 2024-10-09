#!/usr/bin/python3
# work by: odedeyi oladapo olayinka
""" A class with no class or obj attr...

that prevents user: from creating new instance attribute

except: if the new instance attribute is called first_name

"""


class LockedClass:
    """ A class that prevent instance and only allow instance
    with the attribute: first_name
    """
    __slots__ = ["first_name"]