#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = None
    max_value = 0

    for key, value in a_dictionary.items():
        value_int = int(value)
        if value_int > max_value:
            max_value = value_int
            max_value = key
    return max_value
