#!/usr/bin/python3
"""
Test module for Rectangle functions
"""


import unittest
import sys


sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')


from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test class
    """
    def test_01_Rectangle_init(self):
        """when width is should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, -1, 5)
        self.assertRaises(TypeError, Rectangle, True, 5)
        self.assertRaises(TypeError, Rectangle, "ope", 5)

        """when height should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Rectangle, 5, 0)
        self.assertRaises(ValueError, Rectangle, 5, -1)
        self.assertRaises(TypeError, Rectangle, 5, True)
        self.assertRaises(TypeError, Rectangle, 5, "ope")

        """when x should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Rectangle, 5, 4, -1, 5)
        self.assertRaises(TypeError, Rectangle, 5, 4, True, 6)
        self.assertRaises(TypeError, Rectangle, 5, 4, "ope", 6)

        """whem y should raise valueerror and typeerror
        """
        self.assertRaises(ValueError, Rectangle, 5, 4, 1, -5)
        self.assertRaises(TypeError, Rectangle, 5, 4, 6, True)
        self.assertRaises(TypeError, Rectangle, 5, 4, 6, "ope")

        """checking the id when an id is given
        """
        r2 = Rectangle(3, 5, 7, 9, 1999)
        self.assertEqual(r2.id, 1999)

    """
    testing the getter methods
    """
    def test_02_getter(self):
        """Testing getter for id, width, height, x and y
        """
        r3 = Rectangle(3, 5, 7, 9, 8)
        self.assertEqual(r3.id, 8)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 7)
        self.assertEqual(r3.y, 9)

    """
    testing setter methods
    """
    def test_03_setter(self):
        """when the correct type and values are passed
        """
        r4 = Rectangle(3, 5, 7, 9)
        r4.width = 10
        r4.height = 11
        r4.x = 12
        r4.y = 13
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 11)
        self.assertEqual(r4.x, 12)
        self.assertEqual(r4.y, 13)

        """when the wrong type is assigned to each attribute
        """
        with self.assertRaises(TypeError):
            r4.width = "ope"
        with self.assertRaises(TypeError):
            r4.height = True
        with self.assertRaises(TypeError):
            r4.x = "ogun"
        with self.assertRaises(TypeError):
            r4.y = False

        """when the wrong values are assigned to each attribute
        """
        with self.assertRaises(ValueError):
            r4.width = 0
        with self.assertRaises(ValueError):
            r4.height = -1
        with self.assertRaises(ValueError):
            r4.x = -1
        with self.assertRaises(ValueError):
            r4.y = -1937298028

    def test_04_display(self):
        """when x and y are 0
        """
        r5 = Rectangle(5, 3)
        file_name = "/root/alx-higher_level_programming/0x0C-python-almost_a_circle/print_test"
        sys.stdout = open(file_name, 'w')
        r5.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '#####\n#####\n#####\n')

        """when x is a positive integer
        """
        r6 = Rectangle(5, 3, 4, 0)
        sys.stdout = open(file_name, 'w')
        r6.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '    #####\n    #####\n    #####\n')

        """when y is a positive integer
        """
        r7 = Rectangle(5, 3, 0, 4)
        sys.stdout = open(file_name, 'w')
        r7.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        self.assertEqual(file_content, '\n\n\n\n#####\n#####\n#####\n')

        """when both x and y are positive integers
        """
        r8 = Rectangle(5, 3, 3, 4)
        sys.stdout = open(file_name, 'w')
        r8.display()
        sys.stdout.close()
        with open(file_name) as f:
            file_content = f.read()
        display = '\n\n\n\n   #####\n   #####\n   #####\n'
        self.assertEqual(file_content, display)

    """
    Test for the __str__ method
    """
    def test_05_str(self):
        """printing the object
        """
        r9 = Rectangle(3, 4, 5, 6, 45)
        print_object = '[Rectangle] (45) 5/6 - 3/4\n'
        file_name = "/root/alx-higher_level_programming/0x0C-python-almost_a_circle/print_test"
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
        r10 = Rectangle(3, 4, 5, 6)
        r10.update(9, 8)
        self.assertEqual(r10.id, 9)
        self.assertEqual(r10.width, 8)
        r10.update(9, 8, 7)
        self.assertEqual(r10.height, 7)

        """when wrong types are passed through *args
        """
        with self.assertRaises(TypeError):
            r10.update(None, "ope", 3, 4, 5)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 4.5, 6, 8)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 4, False, 6)
        with self.assertRaises(TypeError):
            r10.update(None, 3, 4, 5, 7.5)

        """when the wrong values are passed through *args
        """
        with self.assertRaises(ValueError):
            r10.update(None, 0, 3, 4, 5)
        with self.assertRaises(ValueError):
            r10.update(None, 2, -5, 6, 8)
        with self.assertRaises(ValueError):
            r10.update(None, 2, 3, -6, 5)
        with self.assertRaises(ValueError):
            r10.update(None, 2, 3, 4, -5687)

    """
    Test for update method through kwargs
    """
    def test_07_update_kwargs(self):
        """when incomplete arguments are passed
        """
        r11 = Rectangle(3, 5, 7, 9)
        r11.update(id=7, width=2, y=12)
        self.assertEqual(r11.id, 7)
        self.assertEqual(r11.width, 2)
        self.assertEqual(r11.y, 12)
        self.assertEqual(r11.height, 5)
        self.assertEqual(r11.x, 7)

        """when wrong types are passed through kwargs
        """
        with self.assertRaises(TypeError):
            r11.update(id=7, width="ope", y=12)
        with self.assertRaises(TypeError):
            r11.update(id=7, width=2, y=False)
        with self.assertRaises(TypeError):
            r11.update(id=7, width=2, y=12, height=5.6)
        with self.assertRaises(TypeError):
            r11.update(id=7, width=2, y=12, height=5, x="ope")

        """when wrong values are passed through kwargs
        """
        with self.assertRaises(ValueError):
            r11.update(id=7, width=0, y=12)
        with self.assertRaises(ValueError):
            r11.update(id=7, width=2, y=4, height=-5)
        with self.assertRaises(ValueError):
            r11.update(id=7, width=2, y=-4, height=5)
        with self.assertRaises(ValueError):
            r11.update(id=7, width=2, y=12, height=5, x=-3)

    """
    Test for when args and kwargs are present
    """
    def test_08_update_args_kwargs(self):
        """passing both args and kwargs
        """
        r12 = Rectangle(3, 5, 7)
        r12.update(31, 51, 71, id=32, height=52, x=72, y=82)
        self.assertEqual(r12.id, 31)
        self.assertEqual(r12.width, 51)
        self.assertEqual(r12.height, 71)
        self.assertEqual(r12.x, 7)

    """
    Test for to_dictionary method
    """
    def test_09_to_dictionary(self):
        """when an instance is passed to the method
        """
        r13 = Rectangle(3, 5, 7, 9, 12)
        to_dict = r13.to_dictionary()
        dict_form = {'id': 12, 'width': 3, 'height': 5, 'x': 7, 'y': 9}
        self.assertEqual(to_dict, dict_form)
