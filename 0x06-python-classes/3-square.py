#!/usr/bin/python3
""" define class 'Square'"""


class Square:
    """ class 'Square'"""
    def __init__(self, size=0):
        """ Initialize class 'Square'
        Args: size
        if size not int or < 0, raise Exceptions
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method - returns square area of class 'Square'"""
        return self.__size ** 2
