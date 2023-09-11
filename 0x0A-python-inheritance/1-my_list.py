#!/usr/bin/python3
"""
class MyList inherits from list
"""


class MyList(list):
    """define MyList
    Args: list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
