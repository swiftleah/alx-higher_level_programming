#!/usr/bin/python3
""" Documentation:
    Class 'Square' that defines a square with private instance attribute 'size'
"""


class Square:
    """ class 'Square'"""
    def __init__(self, size):
        """ Initialize new 'Square'
        Args:
        size - private attribute for size of square
        """
        self.__size = size
