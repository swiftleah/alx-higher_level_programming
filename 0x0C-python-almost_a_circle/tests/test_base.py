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

        self.assertTrue(len(Base.to_json_string([rect1_dict])), 52)

    def test_to_json_string_two_rectangle_dict(self):
        rect1 = Rectangle(9, 6, 1, 7, 2)
        rect2 = Rectangle(12, 7, 3, 8, 4)
        rect1_dict = rect1.to_dictionary()
        rect2_dict = rect1.to_dictionary()

        list_dicts = [rect1.to_json_string([rect1_dict]), rect1.to_json_string([rect2_dict])]

        self.assertTrue(len(list_dicts), 106)

    def test_to_json_string_one_square_dict(self):
        sq1 = Square(10, 2, 5, 6)
        sq1_dict = sq1.to_dictionary()

        self.assertTrue(len(Base.to_json_string([sq1_dict])), 39)

    def test_to_json_string_two_square_dict(self):
        sq1 = Square(10, 2, 5, 6)
        sq2 = Square(11, 3, 6, 7)
        sq1_dict = sq1.to_dictionary()
        sq2_dict = sq2.to_dictionary()

        list_squares = [sq1_dict, sq2_dict]

        self.assertTrue(len(Base.to_json_string([list_squares])), 78)

    def test_to_json_string_type_rectangle(self):
        rect1 = Rectangle(9, 6, 1, 7, 2)
        rect1_dict = rect1.to_dictionary()

        self.assertEqual(str, type(Base.to_json_string([rect1_dict])))

    def test_to_json_string_type_square(self):
        sq1 = Square(10, 2, 5, 6)
        sq1_dict = sq1.to_dictionary()

        self.assertTrue(str, type(Base.to_json_string([sq1_dict])))

    def test_to_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_wrong_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class TestBase_save_to_file(unittest.TestCase):
    """ Unittests for Task 17: writes JSON string rep to specified file """
    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

class TestBase_from_json_string(unittest.TestCase):
    """ Unittests for Task 17: returns list of JSON string rep """
    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_square(self):
        input1 = [{'id': 89, 'width': 10, 'height': 4}]
        json_input1 = Square.to_json_string(input1)
        output1 = Square.from_json_string(json_input1)

        self.assertEqual(input1, output1)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

class TestBase_create(unittest.TestCase):
    """ Unittests for Task 18: returns an instance with all
    attributes already set """
    def test_create_rectangle(self):
        r = Rectangle(3, 5, 1)
        r.dict = r.to_dictionary()
        r1 = Rectangle.create(**r.dict)

        self.assertEqual("[Rectangle] (1) 1/0 - 3/5", str(r1))

    def test_create_square(self):
        sq = Square(3, 5, 6, 1)
        sq.dict = sq.to_dictionary()
        sq1 = Square.create(**sq.dict)


        self.assertEqual("[Square] (1) 5/6 - 3", str(sq1))




if __name__ == '__main__':
    unittest.main()
