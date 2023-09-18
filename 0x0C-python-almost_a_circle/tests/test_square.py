#!/usr/bin/python3
""" unittests for square.py """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_update(unittest.TestCase):
    """ Unittest for Task 12: assigns attributes
    args is list of arguments
    kwargs used when args is empty or None """
    def test_update_square_one_arg(self):
        sq1 = Square(6)
        sq1.update(1)

        self.assertEqual("[Square] (1) 0/0 - 6", str(sq1))

    def test_update_square_two_args(self):
        sq1 = Square(6)
        sq1.update(1, 2, 3, 4)

        self.assertEqual("[Square] (1) 3/4 - 2", str(sq1))


class TestSquare_to_dictionary(unittest.TestCase):
    """ unittests for task 14: returns dictionary representation
    of specified shape """
    def test_to_dictionary_square(self):
        sq1 = Square(10, 2, 5, 6)

        self.assertTrue(len(sq1.to_dictionary()), 39)

    def test_to_dictionary_type_square(self):
        sq1 = Square(10, 2, 5, 6)

        self.assertTrue(isinstance(sq1.to_dictionary(), dict))

    def test_to_dictionary_one_updated_square(self):
        sq1 = Square(10, 2, 5, 6)
        sq2 = Square(13, 5, 8, 9)
        sq1_update = sq1.to_dictionary()

        self.assertNotEqual(sq1_update, sq2)

if __name__ == "__main__":
    unittest.main()
