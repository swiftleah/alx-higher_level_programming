#!/usr/bin/python3
"""class BaseGeomtry with Exception messages"""


class BaseGeometry:
    """ define instances:"""
    def area(self):
        """ public instance area - raises Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer-Validator - checks if given correct argument

        Args:
            name: name of parameter, value: value in int
        Raises:
            TypeError & ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
