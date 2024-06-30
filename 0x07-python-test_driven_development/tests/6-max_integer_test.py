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
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begining(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 1, 2]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test a list with a single element."""
        one_element = [4]
        self.assertEqual(max_integer(one_element), 4)

    def test_floats(self):
        """Test a list of floats."""
        floats = [12.3, 4.2, 14.9, 3.1]
        self.assertEqual(max_integer(floats), 14.9)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ['jamie', 'messi', 'Gideon']
        self.assertEqual(max_integer(strings), 'Gideon')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(''), None)


if __name__ == '__main__':
    unittest.main()
