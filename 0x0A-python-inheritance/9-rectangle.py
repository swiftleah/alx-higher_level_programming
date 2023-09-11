#!/usr/bin/python3
"""
class BaseGeomtry with Exception messages
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass to BaseGeometry """
    def __init__(self, width, height):
        """ Initialize self
        Args: width & height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return string repr of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
