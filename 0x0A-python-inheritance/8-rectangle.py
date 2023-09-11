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
