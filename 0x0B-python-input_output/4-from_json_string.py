#!/bin/python3
""" Function from_json_string """


import json


def from_json_string(my_str):
    """ returns object represented by JSON string
    Args: my_str """
    return json.loads(my_str)
