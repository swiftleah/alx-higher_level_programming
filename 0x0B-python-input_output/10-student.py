#!/usr/bin/python3
""" class Student with initialization """


class Student:
    """ class """
    def __init__(self, first_name, last_name, age):
        """ Initialize class
        Args: first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json - retrieves dict representation of student instance
        if attrs is list of strings, only attribute names in list
        to be retrieved """
        if isinstance(attrs, list) and all(isinstance(elements, str)
                                           for elements in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
