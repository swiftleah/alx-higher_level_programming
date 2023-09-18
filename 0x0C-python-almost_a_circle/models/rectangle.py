#!/usr/bin/python3
""" class 'Rectangle' inherited from 'Base' """


from models.base import Base


class Rectangle(Base):
    """ class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize 'Rectangle'
        Args: width, height, x, y, id """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of rectangle """
        return self.width * self.height

    def display(self):
        """ Prints rectangle to stdout handling height & width """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ String representation of rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns each argument to attributes accordingly """
        if args:
            arg_list = list(args)
            if len(arg_list) >= 1:
                self.id = arg_list[0]
            if len(arg_list) >= 2:
                self.width = arg_list[1]
            if len(arg_list) >= 3:
                self.height = arg_list[2]
            if len(arg_list) >= 4:
                self.x = arg_list[3]
            if len(arg_list) >= 5:
                self.y = arg_list[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary rep of 'Rectangle' """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
