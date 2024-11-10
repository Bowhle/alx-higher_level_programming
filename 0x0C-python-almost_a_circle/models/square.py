#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle
""" importing the rectangle from its file loacation ommiting the .py"""


class Square(Rectangle):
    """ A class that inherits from Rectangle with a super inheritment
    from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ the instantation or initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the print function"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ a getter function from width"""
        return self.width

    @size.setter
    def size(self, value):
        """ getter function for the width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ the function assigns attribute"""
        attr = []
        for ele in args:
            attr.append(ele)
        if len(attr) >= 1:
            self.id = attr[0]
        if len(attr) >= 2:
            self.size = attr[1]
        if len(attr) >= 3:
            self.x = attr[2]
        if len(attr) >= 4:
            self.y = attr[3]

        if len(attr) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """ returns a dictionary """
        return {"id": getattr(self, "id"),
                "x": getattr(self, "x"),
                "size": getattr(self, "size"),
                "y": getattr(self, "y")
                }
