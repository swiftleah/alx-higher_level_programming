#!/usr/bin/python3
"""
function print_square
Args: size of square in ints
size must be an int
"""


def print_square(size):
    """
    function print_square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
