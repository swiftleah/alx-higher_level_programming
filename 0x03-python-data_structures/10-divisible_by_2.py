#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for numbers in my_list:
        result.append(numbers % 2 == 0)
    return result
