#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for numbers in matrix:
        new_num = []
        for number in numbers:
            new_num.append(number ** 2)
        new_matrix.append(new_num)

    return new_matrix
