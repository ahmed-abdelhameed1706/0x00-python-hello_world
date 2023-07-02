#!/usr/bin/python3
"""
importing important modules for unit testing
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max_integer(self):
        my_list = [1, 2, 3, 4]
        float_list = [0.4, 1.3, 2.1, 2.2, 0.2]
        mixed_list = [5, 2.4, 4.9, 3]
        another_mixed = [3, 9.7, 5.4, 2, 8]
        string_list = "abcd"
        negative_ints = [-4, -2, -7, -5]
        pos_neg_ints = [1, -9, -2, 3]
        another_negative = [-6, -2, 0, -1]

        self.assertEqual(max_integer(my_list), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(float_list), 2.2)
        self.assertEqual(max_integer(mixed_list), 5)
        self.assertEqual(max_integer(another_mixed), 9.7)
        self.assertEqual(max_integer(string_list), "d")
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer(negative_ints), -2)
        self.assertEqual(max_integer(pos_neg_ints), 3)
        self.assertEqual(max_integer(another_negative), 0)
