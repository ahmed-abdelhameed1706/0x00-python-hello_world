#!/usr/bin/python3
"""
model for unittesting for base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    model for unittesting for base class
    """

    def setUp(self):
        Base.__nb_objects = 0

    def test_id(self):
        """
        method to test all differet possiblities for id
        """
        test = Base()
        self.assertEqual(test.id, 1)
        
        test2 = Base(3)
        self.assertEqual(test2.id, 3)

        test3 = Base()
        test4 = Base(99)
        self.assertEqual(test3.id, 2)
        self.assertEqual(test4.id, 99) 
