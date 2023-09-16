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
    def test_to_json_string_empty_dict(self):
        self.assertEqual("[]", Base.to_json_string([]))
