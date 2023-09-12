#!/usr/bin/python3
""" class_to_json - returns dict description with
simple data structure for JSON serialization of object """


def class_to_json(obj):
    """ define function
    Args: obj """
    return obj.__dict__
