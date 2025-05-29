import number_categories
import unittest
from unittest import TestCase

class TestNumberCategories(TestCase):
	def test_number_categories_function_existence(self):
		number_categories.categorise(10, 15, 21, 30)

	def test_number_categories_function_action(self):
		actual = number_categories.categorise(10, 15, 21, 30)
		expected = (10, 15, 30)
		self.assertEqual(actual, expected)

	def test_number_categories_function_no_inputs_check(self):
		self.assertEqual(number_categories.categorise(), "This array is empty")

	def test_number_categories_function_zero_check(self):
		self.assertEqual(number_categories.categorise(0, 15, 21, 30), (15, 30))
		self.assertEqual(number_categories.categorise(0, 0, 0, 0), "There are no multiples")
	
	def test_number_categories_function_no_multiples_check(self):
		self.assertEqual(number_categories.categorise(11, 16, 21, 31), "There are no multiples")
		self.assertEqual(number_categories.categorise(0, 0, 0, 4), "There are no multiples")
		self.assertEqual(number_categories.categorise(0, -10, 15.01, 19), "There are no multiples")

	def test_number_categories_function_negative_value_check(self):
		self.assertEqual(number_categories.categorise(-10, 15, 21, 30), (15, 30))
		self.assertEqual(number_categories.categorise(-10, -15, -21, -30),  "There are no multiples")

	def test_number_categories_function_floating_number_check(self):
		self.assertEqual(number_categories.categorise(10.1, 15, 21, 30), (15, 30))
		self.assertEqual(number_categories.categorise(10.00001, 15, 21, 30), (15, 30))
		self.assertEqual(number_categories.categorise(10.0, 15, 21, 30), (10, 15, 30))

	def test_number_categories_function_other_datatypes_check(self):
		self.assertRaises(ValueError, number_categories.categorise, (10, "a", 21, 30))
		self.assertRaises(ValueError, number_categories.categorise, (10, True, 21, 30))
		self.assertRaises(ValueError, number_categories.categorise, (10, (), 21, 30))
		self.assertRaises(ValueError, number_categories.categorise, (10, [], 21, 30))

