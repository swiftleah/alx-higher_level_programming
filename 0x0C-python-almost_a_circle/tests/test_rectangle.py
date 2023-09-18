#!/usr/bin/python3
""" unittests for rectangle.py """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_instances(unittest.TestCase):
    """ Unittests for instances of Rectangle """
    def test_inheritence(self):
        r = Rectangle(10, 10, 10, 10)

        self.assertIsInstance(r, Base)

    def test_rectangle_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_id_number_2_rectangles(self):
        r1 = Rectangle(5, 2)
        r2 = Rectangle(7, 3)

        self.assertEqual(r1.id, r2.id - 1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7)


class TestRectangle_area(unittest.TestCase):
    """ Unittests for task 4: returns area of Rectangle """
    def test_area_rectangle(self):
        r = Rectangle(3, 2)

        self.assertEqual(r.area(), 6)

    def test_area_rectangle_five_dimensions(self):
        r = Rectangle(8, 7, 1, 1, 12)

        self.assertEqual(r.area(), 56)

class TestRectangle_display(unittest.TestCase):
    """ Unittests for Task 5: Method display - prints stdout of
    Rectangle instance with '#' """
    def test_display_one_arg(self):
        r = Rectangle(5, 1, 0, 0, 0)
        with self.assertRaises(TypeError):
            r.display(1)
