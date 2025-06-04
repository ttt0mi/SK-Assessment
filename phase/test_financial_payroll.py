import financial_payroll
from financial_payroll import *
import unittest
from unittest import TestCase



class TestFinancialPayroll(TestCase):


	def test_financial_payroll_add_function_existence(self):
		payroll = {}
		details = ("tomide", 10, 9.75, 20, 9)
		add(payroll, details)


	def test_financial_payroll_name_check_function(self):
		name = "Tomide"
		self.assertTrue(name_check(name))


	def test_financial_payroll_hours_worked_check_function(self):
		working_hrs = "10"
		self.assertTrue(hours_worked_check(working_hrs))


	def test_financial_payroll_payments_check_function(self):
		pay_per_hr = "9.75"
		self.assertTrue(payments_check(pay_per_hr))


	def test_financial_payroll_tax_check_function(self):
		tax = "20"
		self.assertTrue(tax_check(tax))


	def test_financial_payroll_add_payroll(self):
		payroll = {}
		details = ("tomide", 10, 9.75, 20, 9)

		actual = add(payroll, details)
		expected = "employee payroll added>>>"
		self.assertEqual(actual, expected)


	def test_financial_payroll_update(self):
		payroll = {}
		details = ("tomide", 10, 9.75, 20, 9)
		add(payroll, details)

		name = "Tomide"
		self.assertTrue(update(payroll, name))

"""

	def test_financial_payroll_view(self):
		payroll = {}
		actual = view(payroll)
		expected = "There are no payrolls available to view"

		self.assertEqual(actual, expected)
"""


