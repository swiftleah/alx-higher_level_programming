#!/usr/bin/python3
""" define class 'Square'"""


class Square:
    """ class 'Square'"""
    def __init__(self, size=0):
        """ Initialize 'Square'
        Args: size
        if size not int or < 0, raises exceptions
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
