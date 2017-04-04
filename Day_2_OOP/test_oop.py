import unittest

from oop import Employee, Manager, Staff

class OOPTest(unittest.TestCase):
	
	def test_staff_class_works(self):
		adams = Staff("Adams Kariuki", 20006257, "15-Jan-2000", "Male", 0124, "I.T.", "Alex Magana")
		self.assertListEqual([adams.name, adams.id_number, adams.date_of_birth, adams.gender, adams.staff_number, adams.department, adams.supervisor], ["Adams Kariuki", 20006257, "15-Jan-2000", "Male", 0124, "I.T.", "Alex Magana"], "Does not work")

	def test_manager_class_works(self):
		alex = Manager("Alex Magana", 32145746, "05-April-2005", "Male", 0100, "I.T.")
		self.assertListEqual([alex.name, alex.id_number, alex.date_of_birth, alex.gender, alex.staff_number, alex.department], ["Alex Magana", 32145746, "05-April-2005", "Male", 0100, "I.T."], "Does not work")