#!/usr/bin/python3
"""
Test module for base.py model
"""


import unittest
import json
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    test suite for base class
    """

    """
    testing for various cases of id
    """
    def test_01_Base_no_id(self):
        """when no id is passed
        """
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

    def test_02_Base_id(self):
        """when an id is passed
        """
        instance2 = Base(5)
        self.assertEqual(instance2.id, 5)

    """
    testing for various inputs to base_to_string function
    """
    def test_03_Base_to_json_string_None(self):
        """when list_dictionaries is None
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_04_Base_to_json_string_empty(self):
        """when list_dictionaries is an empty dictionary
        """
        self.assertEqual(Base.to_json_string({}), "[]")

    def test_05_Base_to_json_string_filled(self):
        """when a dictionary with keys and values is passed
        """
        dictionaries = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        string_rep = Base.to_json_string(dictionaries)
        dict_rep = json.loads(string_rep)
        act_dict = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertEqual(dict_rep, act_dict)

    """
    testing the save_to_file function with Rectangle instances
    """
    def test_06_Base_Rectangle_save_to_file_None(self):
        """when list_objs is None
        """
        rect_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Rectangle.json'
        Rectangle.save_to_file(None)
        with open(rect_file_path, 'r') as rect_file:
            file_content = rect_file.read()
        self.assertEqual(file_content, '[]')

    def test_07_Base_Rectangle_save_to_file_empty(self):
        """when list_objs is empty
        """
        rect_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Rectangle.json'
        Rectangle.save_to_file([])
        with open(rect_file_path, 'r') as rect_file2:
            file_content2 = rect_file2.read()
        self.assertEqual(file_content2, '[]')

    def test_08_Base_Rectangle_save_to_file_nonempty(self):
        """when list_objs is a list of rectangles
        """
        rect_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Rectangle.json'
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect1, rect2])
        with open(rect_file_path, 'r') as rect_file3:
            file_content3 = rect_file3.read()
        converted = json.loads(file_content3)
        dict_1 = {"y": 8, "x": 2, "id": 2, "width": 10, "height": 7}
        dict_2 = {"y": 0, "x": 0, "id": 3, "width": 2, "height": 4}
        act_list = []
        act_list.append(dict_1)
        act_list.append(dict_2)
        self.assertEqual(converted, act_list)

    """
    testing the save_to_file function with Square instances
    """
    def test_09_Base_Square_save_to_file_None(self):
        """when list_objs is None
        """
        sqr_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Square.json'
        Square.save_to_file(None)
        with open(sqr_file_path, 'r') as sqr_file:
            file_content = sqr_file.read()
        self.assertEqual(file_content, '[]')

    def test_10_Base_Square_save_to_file_empty(self):
        """when list_objs is empty
        """
        sqr_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Square.json'
        Square.save_to_file([])
        with open(sqr_file_path, 'r') as sqr_file2:
            file_content2 = sqr_file2.read()
        self.assertEqual(file_content2, '[]')

    def test_11_Base_Square_save_to_file_nonempty(self):
        """when list_objs is a list of squares
        """
        sqr_file_path = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Square.json'
        rect1 = Square(10, 7, 2)
        rect2 = Square(2, 4)
        Square.save_to_file([rect1, rect2])
        with open(sqr_file_path, 'r') as sqr_file3:
            file_content3 = sqr_file3.read()
        converted = json.loads(file_content3)
        dict_1 = {"y": 2, "x": 7, "id": 4, "size": 10}
        dict_2 = {"y": 0, "x": 4, "id": 5, "size": 2}
        act_list = []
        act_list.append(dict_1)
        act_list.append(dict_2)
        self.assertEqual(converted, act_list)

    """
    testing the from_json_string function using various inputs
    """
    def test_12_Base_from_json_string_None(self):
        """when json_string is None
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_13_Base_from_json_string_empty(self):
        """when json_string is an empty string
        """
        self.assertEqual(Base.from_json_string(''), [])

    def test_14_Base_from_json_string_nonempty(self):
        """when json_string is a string list of dictionaries
        """
        string_list = '[{"height": 4, "width": 10, "id": 89},\
            {"height": 7, "width": 1, "id": 7}]'
        dict_1 = {'height': 4, 'width': 10, 'id': 89}
        dict_2 = {'height': 7, 'width': 1, 'id': 7}
        actual_list = []
        actual_list.append(dict_1)
        actual_list.append(dict_2)
        self.assertEqual(Base.from_json_string(string_list), actual_list)

    """
    testing the create class method that creates an instance of a class
    """
    def test_15_Base_create_nonempty(self):
        """when dictionary is not empty
        """
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

    """
    testing the load_from_file function using rectangle instances
    """
    def test_16_Base_Rectangle_load_from_file_nofile(self):
        """when file doesnt exist
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_17_Base_Rectangle_load_from_file_empty(self):
        """when file is empty
        """
        with open('/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Rectangle.json', 'w') as rect_file:
            rect_file.write('')
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_18_Base_Rectangle_load_from_file_list(self):
        """when file contains a string list
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 0, 0, 1999)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        output_list = Rectangle.load_from_file()
        self.assertEqual((output_list[0]).id, 8)
        self.assertEqual((output_list[0]).width, 10)
        self.assertEqual((output_list[0]).height, 7)
        self.assertEqual((output_list[0]).x, 2)
        self.assertEqual((output_list[0]).y, 8)
        self.assertEqual((output_list[1]).id, 1999)
        self.assertEqual((output_list[1]).width, 2)
        self.assertEqual((output_list[1]).height, 4)
        self.assertEqual((output_list[1]).x, 0)
        self.assertEqual((output_list[1]).y, 0)

    """
    testing the load_from_file function using square instances
    """
    def test_19_Base_Square_load_from_file_nofile(self):
        """when file doesnt exist
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_20_Base_Square_load_from_file_empty(self):
        """when file is empty
        """
        with open('/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/Square.json', 'w') as sqr_file:
            sqr_file.write('')
        self.assertEqual(Square.load_from_file(), [])

    def test_21_Base_Square_load_from_file_list(self):
        """when file contains a string list
        """
        r1 = Square(10, 7, 2)
        r2 = Square(4, 0, 0, 1999)
        input_list = [r1, r2]
        Square.save_to_file(input_list)
        output_list = Square.load_from_file()
        self.assertEqual((output_list[0]).id, 11)
        self.assertEqual((output_list[0]).size, 10)
        self.assertEqual((output_list[0]).x, 7)
        self.assertEqual((output_list[0]).y, 2)
        self.assertEqual((output_list[1]).id, 1999)
        self.assertEqual((output_list[1]).size, 4)
        self.assertEqual((output_list[1]).x, 0)
        self.assertEqual((output_list[1]).y, 0)
