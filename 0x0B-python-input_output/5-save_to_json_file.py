#!/usr/bin/python3
""" Function save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to text file using JSON representation
    Args: my_obj, filename """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
