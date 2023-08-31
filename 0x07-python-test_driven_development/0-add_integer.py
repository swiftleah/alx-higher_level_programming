#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Define function add_integer
    Args:
    int a
    int b = 98
    if a or b = float, cast to int
    if a or b not int, raise TypeError
    """
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
