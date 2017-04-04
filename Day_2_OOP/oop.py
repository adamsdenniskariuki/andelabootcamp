# class demonstrating encapsulation
class Employee(object):

	def __init__(self, name, id_number, gender, staff_number, department):
		self.name = name
		self.id = id_number
		self.gender = gender
		self.staff_number = staff_number
		self.department = department

	def salary(self):
		return 5000

	def annual_leave(self):
		return 30

# class inheriting from the Employee class
class Manager(Employee):

	def __init__(self, name, id_number, gender, staff_number, department):
		super(Manager, self).__init__(name, id_number, gender, staff_number, department)

	# function demonstrating polymorphism
	def salary(self):
		return 75000	

# class inheriting from the Employee class
class Staff(Employee):

	def __init__(self, name, id_number, gender, staff_number, department, supervisor):
		super(Staff, self).__init__(name, id_number, gender, staff_number, department)
		self.supervisor = supervisor

	# function demonstrating polymorphism
	def salary(self):
		return 30000

adams = Staff("Adams Kariuki", 20006257, "Male", 0124, "I.T.", "Alex Magana")
print adams.annual_leave(), adams.supervisor, adams.name

alex = Manager("Alex Magana", 32145746, "Male", 0100, "I.T.")
print alex.annual_leave(), alex.department, alex.name

