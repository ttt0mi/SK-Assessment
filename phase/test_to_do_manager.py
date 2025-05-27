import to_do_manager
from to_do_manager import *

import unittest
from unittest import TestCase


class TestToDoManager(TestCase):

	def test_to_do_manager_existence(self):
		tasks = {}
		add(tasks, "Buy Gadjets")


	def test_to_do_manager_add_function(self):

		tasks = {}
		self.assertEqual(add(tasks, "Gadget Shopping"), "Added")


	def test_to_do_manager_userInput_check(self):

		self.assertEqual(userinput_check('1'), True)
		self.assertEqual(userinput_check('  '), "Input cannot be empty, Try again")
		self.assertEqual(userinput_check('ab'), "Invalid character. Pick a number")

	
	def test_to_do_manager_view_all_tasks(self):

		tasks = {}
		add(tasks, "Gadget Shopping")

		self.assertEqual(view_all(tasks),  {'Gadget Shopping': 'Incomplete'})


	def test_to_do_manager_mark_a_task(self):

		tasks = {}
		add(tasks, "Gadget Shopping")
		mark_task = '1'

		self.assertEqual(mark(tasks, mark_task), "Task 1 completed")
		


	def test_to_do_manager_delete_a_task(self):

		tasks = {}
		add(tasks, "Gadget Shopping")
		delete_task = '1'

		self.assertEqual(delete(tasks, delete_task), "Task 1 deleted")

