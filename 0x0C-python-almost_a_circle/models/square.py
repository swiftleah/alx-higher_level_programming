#!/usr/bin/python3
""" class Square that inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize class Square
        Args: size, x, y, id """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter for size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size of square """
        self.width = value
        self.height = value
