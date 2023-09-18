#!/usr/bin/python3
""" unittests for base.py """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_to_json_string(unittest.TestCase):
    """ Unittests for Task 15: returns JSON string rep
    of list_dicitonaries """
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_one_rectangle_dict(self):
        rect1 = Rectangle(9, 6, 1, 7, 2)
        rect1_dict = rect1.to_dictionary()

        rect1_json = rect1.to_json_string([rect1_dict])

        self.assertEqual(len(rect1_json), 52)

    def test_to_json_string_two_rectangle_dict(self):
        rect1 = Rectangle(9, 6, 1, 7, 2)
        rect2 = Rectangle(12, 7, 3, 8, 4)
        rect1_dict = rect1.to_dictionary()
        rect2_dict = rect1.to_dictionary()

        list_dicts = [rect1.to_json_string([rect1_dict]), rect1.to_json_string([rect2_dict])]

        self.assertTrue(len(list_dicts), 106)
