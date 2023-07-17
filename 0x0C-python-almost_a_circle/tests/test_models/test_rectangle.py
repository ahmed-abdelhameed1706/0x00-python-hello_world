#!/usr/bin/python3
"""
model to test rectangle methods
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class to test rectangle methods
    """

    def test_init(self):
        """
        test initializing of rectangle
        """
        test = Rectangle(1, 2)
        self.assertEqual(test.id, 1)
        self.assertEqual(test.width, 1)
        self.assertEqual(test.height, 2)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)

        with self.assertRaises(AttributeError):
            test = Rectangle()

    def test_validation(self):
        """
        test validation of rectangle attributes
        """
        with self.assertRaises(TypeError):
            test1 = Rectangle("a", 2, 4, 5)
            test2 = Rectangle(1, "a", 4, 5)
            test3 = Rectangle(1, 2, "a", 5)
            test4 = Rectangle(1, 2, 4, "a")
            test5 = Rectangle("a", 2, 4, "a")

        with self.assertRaises(ValueError):
            test1 = Rectangle(0, 1, 2, 3)
            test2 = Rectangle(1, 0, 2, 3)
            test3 = Rectangle(1, 1, -2, 3)
            test4 = Rectangle(0, 1, 2, -3)
            test5 = Rectangle(1, 1, 2, -3)
