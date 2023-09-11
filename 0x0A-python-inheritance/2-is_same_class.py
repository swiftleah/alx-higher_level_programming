#!/usr/bin/python3
"""
is_same checks if object is same instance as specified class
"""


def is_same_class(obj, a_class):
    """ define function
    Args: obj
    a_class - class it is supposed to be instance of
    """
    return type(obj) == a_class
