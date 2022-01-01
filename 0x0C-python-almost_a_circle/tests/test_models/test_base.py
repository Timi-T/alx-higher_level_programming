#!/usr/bin/python3
"""
test module for base.py model
"""


import unittest
import sys

sys.path.insert(0, 'root/alx-higher_level_programming/0x0C-python-almost_a_circle/models/base.py')


from models.base import Base


class TestBase(unittest.TestCase):
    """
    test suite for base class
    """

    def test_Base(self):
        instance1 = Base()
        instance2 = Base(5)
        self.assertEqual(instance1.id, 1)
