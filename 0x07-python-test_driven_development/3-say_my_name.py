#!/usr/bin/python3
"""
Function say_my_name
Args: first_name & Last_name
if not strings, raise Exception
"""


def say_my_name(first_name, last_name=""):
    """
    define say_my_name function
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        full_name = first_name + " " + last_name
        print("My name is {}".format(full_name))
