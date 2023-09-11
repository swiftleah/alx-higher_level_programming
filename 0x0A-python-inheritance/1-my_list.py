#!/usr/bin/python3
"""
class MyList inherits from list
"""


class MyList(list):
    """define MyList
    Args: list
    """
    def print_sorted(self):
        list_sorted = sorted(self)
        print(list_sorted)
