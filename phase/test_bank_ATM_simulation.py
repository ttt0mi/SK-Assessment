import bank_ATM_simulation
from bank_ATM_simulation import *
import unittest
from unittest import TestCase




class TestBankATMSimulation(TestCase):

	def test_bank_ATM_simulation_account_balance_check_existence(self):
		account_balance = "20000"
		account_balance_check(account_balance)


	def test_bank_ATM_simulation_amount_check_existence(self):
		account_balance = 20000
		amount = "10000"
		amount_check(account_balance, amount)


	def test_bank_ATM_simulation_withdraw_function_existence(self):
		transactions = []
		account_balance = 20000
		amount = 10000
		withdraw(account_balance, transactions, amount)


	def test_bank_ATM_simulation_account_balance_check(self):
		account_balance = "20000"
		actual = account_balance_check(account_balance)
		expected = 20000.0
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_account_balance_check_empty(self):
		account_balance = ""
		actual = account_balance_check(account_balance)
		expected = "account balance cannot be empty"
		self.assertEqual(actual, expected)

		account_balance = "   "
		actual = account_balance_check(account_balance)
		expected = "account balance cannot be empty"
		self.assertEqual(actual, expected)
	

	def test_bank_ATM_simulation_account_balance_check_nondigits(self):
		account_balance = "200p00"
		actual = account_balance_check(account_balance)
		expected = "invalid characters present"
		self.assertEqual(actual, expected)

		account_balance = "2000.00.00"
		actual = account_balance_check(account_balance)
		expected = "invalid characters present"
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_account_balance_check_zero(self):
		account_balance = "00000"
		actual = account_balance_check(account_balance)
		expected = "account balance cannot start with 0"
		self.assertEqual(actual, expected)

		account_balance = "020000.00"
		actual = account_balance_check(account_balance)
		expected = "account balance cannot start with 0"
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_account_balance_check_negative(self):
		account_balance = "-20000.0"
		actual = account_balance_check(account_balance)
		expected = "account balance must be a positive number"
		self.assertEqual(actual, expected)

		account_balance = "-8755.00"
		actual = account_balance_check(account_balance)
		expected = "account balance must be a positive number"
		self.assertEqual(actual, expected)




	def test_bank_ATM_simulation_amount_check_function(self):
		account_balance = 20000
		amount = "10000"
		actual = amount_check(account_balance, amount)
		expected = 10000.0
		self.assertEqual(actual, expected)

	
	def test_bank_ATM_simulation_amount_check_empty(self):
		account_balance = 20000
		amount = ""
		actual = amount_check(account_balance, amount)
		expected = "amount cannot be empty"
		self.assertEqual(actual, expected)

		account_balance = 20000
		amount = "    "
		actual = amount_check(account_balance, amount)
		expected = "amount cannot be empty"
		self.assertEqual(actual, expected)

	
	def test_bank_ATM_simulation_amount_check_nondigits(self):
		account_balance = 20000
		amount = "10@000"
		actual = amount_check(account_balance, amount)
		expected = "invalid characters present"
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_amount_check_negative(self):
		account_balance = 20000
		amount = "-20000"
		actual = amount_check(account_balance, amount)
		expected = "invalid amount entered"
		self.assertEqual(actual, expected)
	
	
	def test_bank_ATM_simulation_amount_check_zero(self):
		account_balance = 20000
		amount = "0000"
		actual = amount_check(account_balance, amount)
		expected = "amount cannot start with 0"
		self.assertEqual(actual, expected)

		account_balance = 20000
		amount = "010000"
		actual = amount_check(account_balance, amount)
		expected = "amount cannot start with 0"
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_amount_check_banking_rules(self):
		account_balance = 50000
		amount = "25000"
		actual = amount_check(account_balance, amount)
		expected = "maximum withdrawal limit reached"
		self.assertEqual(actual, expected)

		account_balance = 20000
		amount = "2300"
		actual = amount_check(account_balance, amount)
		expected = "invalid amount, only multiples of £500/£1000 allowed"
		self.assertEqual(actual, expected)

		account_balance = 20000
		amount = "19000"
		actual = amount_check(account_balance, amount)
		expected = "invalid amount, cannot withdraw more than 90% of account balance"
		self.assertEqual(actual, expected)




	def test_bank_ATM_simulation_accurate_results1(self):
		transactions = []
		account_balance = 20000
		amount = 10000
		actual = withdraw(account_balance, transactions, amount)
		expected = (9900.0, "Transaction Successful")
		self.assertEqual(actual, expected)


	def test_bank_ATM_simulation_accurate_results2(self):
		transactions = []
		account_balance = 50000
		amount = 20000
		actual = withdraw(account_balance, transactions, amount)
		expected = (29900.0, "Transaction Successful")
		self.assertEqual(actual, expected)



