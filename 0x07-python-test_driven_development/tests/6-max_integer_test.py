#!/usr/bin/python3
# 6-max_integer_test.py
# Gideon O Addo
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_max_at_end(self):
        """Test a list with an end value"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test a list with max number in the middle"""
        self.assertEqual(max_integer([1, 4, 3]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 2.2, 4.4, 3.3]), 4.4)

    def test_with_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_mixed_types(self):
        """Test a list with mixed types (int and float)"""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_large_numbers(self):
        """Test a list with very large numbers"""
        self.assertEqual(
                max_integer(
                    [1000000000, 2000000000, 3000000000, 4000000000]
                    ), 4000000000
                )

    """def test_list_with_none(self):
        # Test a list with None values should raise TypeError
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_non_iterable(self):
        # Test non-iterable input should raise TypeError
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_string_elements(self):
        # Test a list of strings should raise TypeError
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])
    """


if __name__ == '__main__':
    unittest.main()
