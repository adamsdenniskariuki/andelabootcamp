import unittest
from loan_calculator import loan_calculator

#class to hold the test cases for the loan calculator
class LoanCalculator(unittest.TestCase):

	#test to determine if the loan calculator works
	def test_it_works(self):
		self.assertEquals(loan_calculator(100000, 12, 12), 112000)

	#test to ensure the user inputs are integers or decimals is validated
	def test_inputs(self):
		self.assertEquals(loan_calculator("12000", "12", "45"), 'invalid input')

	#test to ensure the amount is validated
	def test_amount(self):
		self.assertEquals(loan_calculator(0, 12, 10), 'invalid amount')	

	#test to ensure time is validated
	def test_time(self):
		self.assertEquals(loan_calculator(100000, 12, -10), 'invalid time')

	#test to ensure rate is validated
	def test_rate(self):
		self.assertEquals(loan_calculator(100000, -18, 10), 'invalid rate')

