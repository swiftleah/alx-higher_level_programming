#!/usr/bin/python3
""" unittests for square.py """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_to_dictionary(unittest.TestCase):
    """ unittests for task 14: returns dictionary representation
    of specified shape """
    def test_to_dictionary_square(self):
        sq1 = Square(10, 2, 5, 6)

        self.assertTrue(len(sq1.to_dictionary()), 39)

    def test_to_dictionary_type_square(self):
        sq1 = Square(10, 2, 5, 6)

        self.assertTrue(isinstance(sq1.to_dictionary(), dict))
