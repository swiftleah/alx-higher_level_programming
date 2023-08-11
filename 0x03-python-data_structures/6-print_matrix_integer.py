#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column_idx, value in enumerate(row):
            if column_idx < len(row) - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}$".format(value))
