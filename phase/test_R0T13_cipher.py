import R0T13_cipher
from R0T13_cipher import *

import unittest
from unittest import TestCase


class TestToDoManager(TestCase):

	def test_R0T13_cipher_existence(self):
		sample_input = "Hello, World!"
		encrypt(sample_input)

	