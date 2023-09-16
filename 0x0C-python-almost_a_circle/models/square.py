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

    def update(self, *args, **kwargs):
        """ assigns attributes """
        if args:
            arg_list = list(args)
            if len(arg_list) >= 1:
                self.id = arg_list[0]
            if len(arg_list) >= 2:
                self.size = arg_list[1]
            if len(arg_list) >= 3:
                self.x = arg_list[2]
            if len(arg_list) >= 4:
                self.y = arg_list[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
