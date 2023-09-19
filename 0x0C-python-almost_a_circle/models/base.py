#!/usr/bin/python3
""" class Base - will be the base of all other classes """


import json
import csv


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
    def to_csv_row(instance):
        """ Converts an instance to a row of comma seperated values """
        cls_name = instance.__class__.__name__
        if cls_name == "Rectangle":
            return [
                    instance.id, instance.width, instance.height,
                    instance.x, instance.y
                    ]
        elif cls_name == "Square":
            return [instance.id, instance.size, instance.x, instance.y]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a list of objects to specified CSV file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(cls.to_csv_row(obj))

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize objects from specified CSV file - reads them """
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]),
                                  int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]),
                                  int(row[3]), int(row[0]))
                    obj_list.append(obj)
        except FileNotFoundError:
            pass
        return obj_list

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

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string rep json_string """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            initial = cls(1, 1)
        elif cls.__name__ == 'Square':
            initial = cls(1)

        initial.update(**dictionary)
        return initial

    @classmethod
    def load_from_file(cls):
        """ returns list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_data = file.read()
                dictionary_list = cls.from_json_string(json_data)
                instance_list = [cls.create(**dictionary) for
                                 dictionary in dictionary_list]
            return instance_list
        except FileNotFoundError:
            return []
