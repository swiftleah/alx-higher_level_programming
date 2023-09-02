#!/usr/bin/python3
"""
Define function matrix_divided
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(x / div, 2) for x in row] for row in matrix]

    return result
