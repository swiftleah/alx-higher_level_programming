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
            return {key: getattr(self, key) for key in attrs if
                    hasattr(self, eyk)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the student instance """
        for key, value in json.items():
            setattr(self, key, value)
