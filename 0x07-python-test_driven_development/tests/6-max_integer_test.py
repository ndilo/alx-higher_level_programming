#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -4, 0]), 2)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 2, 1, 3]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

if __name__ == "__main__":
    unittest.main()
