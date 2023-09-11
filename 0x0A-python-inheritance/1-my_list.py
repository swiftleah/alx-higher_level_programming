#!/usr/bin/python3
"""
class MyList inherits from list
"""


class MyList(list):
    """define MyList
    Args: list
    """
    def print_sorted(self):
        """ print_sorted
        Args: self
        prints list in order """
        print(sorted(self))
