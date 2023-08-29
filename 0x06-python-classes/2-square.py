#!/usr/bin/python3
""" Define class 'Square' based on task 1"""


class Square:
    """ class 'Square'"""
    def __init__(self, size=0):
        """ Initialize 'Square'
        Args: size = 0
        if size not int or < 0, raise Exceptions
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
