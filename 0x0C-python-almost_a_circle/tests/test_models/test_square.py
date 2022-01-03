#!/usr/bin/python3
"""
Test module for Rectangle functions
"""


import unittest
import sys


sys.path.append('/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/models')


Square = __import__("square").Square


class TestRectangle(unittest.TestCase):
    """
    Test class
    """
    def test_01_Square_init(self):
        """when size should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, "ope")

        """when x should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Square, 5, -1)
        self.assertRaises(TypeError, Square, 5, True)
        self.assertRaises(TypeError, Square, 5, "ope")
        self.assertRaises(TypeError, Square, 4, 6.4)

        """whem y should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Square, 5, 4, -5)
        self.assertRaises(TypeError, Square, 5, 4, True)
        self.assertRaises(TypeError, Square, 5, 4, "ope")

        """checking the id when an id is given
        """
        r2 = Square(3, 5, 7, 9)
        self.assertEqual(r2.id, 9)

    """
    testing the getter methods
    """
    def test_02_getter(self):
        """Testing getter for id, width, height, x and y
        """
        r3 = Square(3, 5, 7, 9)
        self.assertEqual(r3.id, 9)
        self.assertEqual(r3.size, 3)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 7)

    """
    testing setter methods
    """
    def test_03_setter(self):
        """when the correct type and values are passed
        """
        r4 = Square(3, 5, 7, 9)
        r4.size = 11
        r4.x = 12
        r4.y = 13
        self.assertEqual(r4.size, 11)
        self.assertEqual(r4.x, 12)
        self.assertEqual(r4.y, 13)

        """when the wrong type is assigned to each attribute
        """
        with self.assertRaises(TypeError):
            r4.size = "ope"
        with self.assertRaises(TypeError):
            r4.size = True
        with self.assertRaises(TypeError):
            r4.x = "ogun"
        with self.assertRaises(TypeError):
            r4.y = False

        """when the wrong values are assigned to each attribute
        """
        with self.assertRaises(ValueError):
            r4.size = 0
        with self.assertRaises(ValueError):
            r4.size = -1
        with self.assertRaises(ValueError):
            r4.x = -1
        with self.assertRaises(ValueError):
            r4.y = -1937298028

    def test_04_display(self):
        """when x and y are 0
        """
        r5 = Square(5)
        file_name = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/test'
        sys.stdout = open(file_name, 'w')
        r5.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '#####\n#####\n#####\n#####\n#####\n')

        """when x is a positive integer
        """
        r6 = Square(3, 3)
        sys.stdout = open(file_name, 'w')
        r6.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '   ###\n   ###\n   ###\n')

        """when y is a positive integer
        """
        r7 = Square(3, 0, 3)
        sys.stdout = open(file_name, 'w')
        r7.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '\n\n\n###\n###\n###\n')

        """when both x and y are positive integers
        """
        r8 = Square(3, 3, 4)
        sys.stdout = open(file_name, 'w')
        r8.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        display = '\n\n\n\n   ###\n   ###\n   ###\n'
        self.assertEqual(file_content, display)

    """
    Test for the __str__ method
    """
    def test_05_str(self):
        """printing the object
        """
        r9 = Square(3, 4, 5, 13)
        print_object = '[Square] (13) 4/5 - 3\n'
        file_name = '/root/alx-higher_level_programming\
/0x0C-python-almost_a_circle/test'
        sys.stdout = open(file_name, 'w')
        print(r9)
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, print_object)

    """
    Test for update method through args
    """
    def test_06_update_args(self):
        """when we have incomplete arguments to update
        """
        r10 = Square(3, 4, 5)
        r10.update(9, 8)
        self.assertEqual(r10.id, 9)
        self.assertEqual(r10.size, 8)
        r10.update(9, 8, 7)
        self.assertEqual(r10.x, 7)

        """when wrong types are passed through *args
        """
        with self.assertRaises(TypeError):
            r10.update(None, "ope", 3, 4)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 4.5, 6)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 4, False)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 5.6, 5)

        """when the wrong values are passed through *args
        """
        with self.assertRaises(ValueError):
            r10.update(None, 0, 3, 4)
        with self.assertRaises(ValueError):
            r10.update(None, -5, 6, 8)
        with self.assertRaises(ValueError):
            r10.update(None, 2, 3, -6)
        with self.assertRaises(ValueError):
            r10.update(None, 2, 3, -5687)

    """
    Test for update method through kwargs
    """
    def test_07_update_kwargs(self):
        """when incomplete arguments are passed
        """
        r11 = Square(3, 5, 7)
        r11.update(id=7, size=2, y=12)
        self.assertEqual(r11.id, 7)
        self.assertEqual(r11.size, 2)
        self.assertEqual(r11.y, 12)
        self.assertEqual(r11.x, 5)

        """when wrong types are passed through kwargs
        """
        with self.assertRaises(TypeError):
            r11.update(id=7, size="ope", y=12)
        with self.assertRaises(TypeError):
            r11.update(id=7, size=2, y=False)
        with self.assertRaises(TypeError):
            r11.update(id=7, y=12, size=5.6)
        with self.assertRaises(TypeError):
            r11.update(id=7, y=12, x="ope")

        """when wrong values are passed through kwargs
        """
        with self.assertRaises(ValueError):
            r11.update(id=7, size=0, y=12)
        with self.assertRaises(ValueError):
            r11.update(id=7, y=23, size=-5)
        with self.assertRaises(ValueError):
            r11.update(id=7, y=-4, x=8)
        with self.assertRaises(ValueError):
            r11.update(id=7, size=2, y=12, x=-432)

    """
    Test for when args and kwargs are present
    """
    def test_08_update_args_kwargs(self):
        """passing both args and kwargs
        """
        r12 = Square(3, 5, 7)
        r12.update(31, 51, 71, id=32, size=52, x=72, y=82)
        self.assertEqual(r12.id, 31)
        self.assertEqual(r12.size, 51)
        self.assertEqual(r12.x, 71)
        self.assertEqual(r12.y, 7)

    """
    Test for to_dictionary method
    """
    def test_09_to_dictionary(self):
        """when an instance is passed to the method
        """
        r13 = Square(3, 5, 7, 15)
        to_dict = r13.to_dictionary()
        dict_form = {'id': 15, 'size': 3, 'x': 5, 'y': 7}
        self.assertEqual(to_dict, dict_form)
