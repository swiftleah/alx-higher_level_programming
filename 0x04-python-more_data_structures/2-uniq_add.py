#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_int = set()
    result = 0

    for num in my_list:
        if num not in unique_int:
            unique_int.add(num)
            result += num
    return result
