#!/usr/bin/python3
"""
inherits_from - returns True of obj is instance of class that inherited
from specified class
"""


def inherits_from(obj, a_class):
    """
    define function
    Args: obj, a_class
    Returns: True if obj is instance of base class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
