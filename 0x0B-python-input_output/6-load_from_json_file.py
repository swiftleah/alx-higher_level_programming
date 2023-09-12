#!/usr/bin/python3
""" Function load_from_json """


import json


def load_from_json_file(filename):
    """ creates an object from a JSON file
    Args: filename """
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.load(file)
        return obj
