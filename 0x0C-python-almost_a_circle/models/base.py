#!/bin/usr/python3
""" class Base - will be the base of all other classes """


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string rep of argument
        Arg: list_dictionaries - list of dicts """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_list_dictionaries = json.dumps(list_dictionaries)
            return json_list_dictionaries

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string rep of list_objs to file """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as file:
            json_data = cls.to_json_string([obj.to_dictionary() for
                                            obj in list_objs])
            file.write(json_data)
