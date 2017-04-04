# class demonstrating encapsulation
class Employee(object):

	#private
	__salaryconstant = 1000
	__workingdays = 20
	__annualleave = 30

	def __init__(self, name, id_number, date_of_birth, gender, staff_number, department):
		self.name = name
		self.id_number = id_number
		self.date_of_birth = date_of_birth
		self.gender = gender
		self.staff_number = staff_number
		self.department = department

	def salary(self):
		return __calculate_salary()

	def annual_leave(self):
		return self.__annualleave

	def __calculate_salary(self):
		return self.__salaryconstant * self.__workingdays

# class inheriting from the Employee class
class Manager(Employee):

	def __init__(self, name, id_number, date_of_birth, gender, staff_number, department):
		super(Manager, self).__init__(name, id_number, date_of_birth, gender, staff_number, department)

	# function demonstrating polymorphism
	def salary(self):
		return 75 * 1000	

# class inheriting from the Employee class
class Staff(Employee):

	def __init__(self, name, id_number, date_of_birth, gender, staff_number, department, supervisor):
		super(Staff, self).__init__(name, id_number, date_of_birth, gender, staff_number, department)
		self.supervisor = supervisor

	# function demonstrating polymorphism
	def salary(self):
		return 30 * 1000

adams = Staff("Adams Kariuki", 20006257, "15-Jan-2000", "Male", 0124, "I.T.", "Alex Magana")
print adams.annual_leave(), adams.supervisor, adams.name, adams.salary(), adams.id_number

alex = Manager("Alex Magana", 32145746, "05-April-2005", "Male", 0100, "I.T.")
print alex.annual_leave(), alex.department, alex.name, alex.salary()

