#!/usr/bin/python3
""" class_to_json - returns dict description with
simple data structure for JSON serialization of object """


import json


def class_to_json(obj):
    """ define function
    Args: obj """
    def serialize_value(value):
        """ Checks what kind of value 'value' is """
        if isinstance(value, (int, str, bool, type(None))):
            return value
        elif isinstance(value, list):
            return [serialize_value(item) for item in value]
        elif isinstance(value, dict):
            return {key: serialize_value(val) for key, val in value.items()}
        elif hasattr(value, '__dict__'):
            return class_to_json(value)
        else:
            raise ValueError("Unsupported data type: {}".format(type(value).__name__))

    if hasattr(obj, '__dict__'):
        serialized = {}
        for key, value in obj.__dict__.items():
            serialized[key] = serialize_value(value)
        return serialized
    else:
        return 0
