#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ class where == and != are inverted """
    def __eq__(self, other):
        """ Equal to method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal to method"""
        return super().__eq__(other)
