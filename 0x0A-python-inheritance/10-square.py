#!/usr/bin/python3
"""
class BaseGeomtry with Exception messages
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size):
        """ Initialize Square
        Args: size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
