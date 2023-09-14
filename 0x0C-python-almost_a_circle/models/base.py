#!/bin/usr/python3
""" class Base - will be the base of all other classes """


class Base:
    """ class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class
        Args: id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
