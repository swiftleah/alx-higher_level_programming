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

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 1, 1, 3).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 1, 1, 3).__height)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 1, 1, 3).__y)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 1, 1, 3).__x)

    def test_width_getter(self):
        r = Rectangle(2, 3, 0, 0, 1)

        self.assertEqual(r.width, 2)

    def test_width_setter(self):
        r = Rectangle(2, 3, 0, 0, 1)
        r.width = 5

        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        r = Rectangle(2, 3, 0, 0, 1)

        self.assertEqual(r.height, 3)

    def test_height_setter(self):
        r = Rectangle(2, 3, 0, 0, 1)
        r.height = 10

        self.assertEqual(r.height, 10)

    def test_x_getter(self):
        r = Rectangle(2, 3, 0, 0, 1)

        self.assertEqual(r.x, 0)

    def test_x_setter(self):
        r = Rectangle(2, 3, 0, 0, 1)
        r.x = 10

        self.assertEqual(r.x, 10)

    def test_y_getter(self):
        r = Rectangle(2, 3, 0, 0, 1)

        self.assertEqual(r.y, 0)

    def test_y_setter(self):
        r = Rectangle(2, 3, 0, 0, 1)
        r.y = 15

        self.assertEqual(r.y, 15)


class TestRectangle_width(unittest.TestCase):
    """ Unittests for width of Rectangle """
    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 6)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.1, 1)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hi", 1)


class TestRectangle_height(unittest.TestCase):
    """ Unittests for height of Rectangle """
    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 9.9)

    def test_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "h")


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
