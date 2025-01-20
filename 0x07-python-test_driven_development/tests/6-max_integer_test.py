#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test case for the max_integer function
    check if the function returns the max 
    integer in a list
    """

    def test_max_num(self):
        """ Test if the function correctly identifies
            maximum number from the list
        """
        my_list = [1, 2, 3, 4]
        result = max_integer(my_list)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list"""
        my_list = []
        result = max_integer(my_list)
        self.assertIsNone

    def test_one_element(self):
        """Test with a single Element"""
        my_list = [7]
        result = max_integer(my_list)
        self.assertEqual(result, 7)

    def test_all_negative(self):
        """Test with all negative numbers."""
        my_list = [-1, -2, -3, -4]
        result = max_integer(my_list)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        my_list = [-1, 2, -3, 4]
        result = max_integer(my_list)
        self.assertEqual(result, 4)

    def test_same_elements(self):
        """Test with a list where all elements are the same."""
        my_list = [5, 5, 5, 5]
        result = max_integer(my_list)
        self.assertEqual(result, 5)
