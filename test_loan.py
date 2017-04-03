import unittest
from loan_calculator import loan_calculator

class LoanCalculator(unittest.TestCase):
	#def test_accepts_integer_values(self):
	#	self.assertEquals(loan_calculator(), )

	def test_it_works(self):
		self.assertEquals(loan_calculator(100000, 12,12), 112000)

	def test_time(self):
		self.assertEquals(loan_calculator(100000, 12, -10), 'invalid time')