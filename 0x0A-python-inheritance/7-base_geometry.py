#!/usr/bin/python3
"""class BaseGeomtry with Exception messages"""


class BaseGeometry:
    """ define instances:"""
    def area(self):
        """ public instance area
        Args:
            self
        Return:
            raise Exceptions where needed
        """
        raise Exception("area() is not implmeneted")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
