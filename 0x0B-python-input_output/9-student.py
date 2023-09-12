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

    def to_json(self):
        """ to_json - returns dict representation
        of student instance """
        return self.__dict__
