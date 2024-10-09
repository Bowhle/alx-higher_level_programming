#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('max_integer_6').max_integer  # Updated import statement


class TestMaxInteger(unittest.TestCase):
    """A unit test class that inherits from unittest.TestCase"""

    def test_ord_list(self):
        """Test ordered list to see if it returns the highest"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_uord_list(self):
        """Test an unordered list and see if it returns the highest"""
        self.assertEqual(max_integer([7, 2, 1, 3]), 7)

    def test_somany(self):
        """Test both float and negative numbers"""
        self.assertEqual(max_integer([2.0, 5.9, -2]), 5.9)
        self.assertEqual(max_integer([-2.6, -0.066, -899]), -0.066)

    def test_empty(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test a list with just one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_string_elements(self):
        """Test a list of strings, should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer(["a", "c", "b"])

    def test_mixed_elements(self):
        """Test a list with mixed types (int and str), should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

    def test_floats_and_ints(self):
        """Test a list with both floats and ints"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

if __name__ == "__main__":
    unittest.main()
