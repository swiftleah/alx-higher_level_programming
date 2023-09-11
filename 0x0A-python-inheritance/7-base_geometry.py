#!/usr/bin/python3
"""class BaseGeomtry with Exception messages"""


class BaseGeometry:
    """ define instances:"""
    def area(self):
        """ public instance area - raises Exception
        """
        raise Exception("area() is not implmeneted")

    def integer_validator(self, name, value):
        """
        Integer-Validator - checks if given correct argument
        Args: name & value
        Int must be an int & cannot be <= 0, otherwise Exceptions are raised
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
