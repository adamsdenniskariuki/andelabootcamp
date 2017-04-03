import unittest
from prime import gen_prime

#class to hold the test cases for the loan calculator
class PrimeTest(unittest.TestCase):
	
	# test if it works
	def test_it_works(self):
		self.assertEquals(gen_prime(7), [2, 3, 5, 7])

	# test for negative input
	def test_negative_input(self):
		self.assertEquals(gen_prime(-5), 'Input cannot be negative')

	# test for integer inputs
	def test_integer(self):
		self.assertEquals(gen_prime("20"), 'Input must be an integer')

	# test for empty inputs
	def test_empty_inputs(self):
		self.assertEquals(gen_prime(""), 'Input cannot be empty')

	# test output of function is a list
	def test_output(self):
		self.assertIsInstance(gen_prime(20), list, 'The output must be a list')