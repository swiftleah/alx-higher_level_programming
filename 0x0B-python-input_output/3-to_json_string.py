#!/usr/bin/python3
""" to_json_string function - returns JSON string of object """


import json


def to_json_string(my_obj):
    """ Define function
    Args: obj """
    return json.dumps(my_obj)
