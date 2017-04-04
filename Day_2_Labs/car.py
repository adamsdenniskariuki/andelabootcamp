# class to test the car object

class Car(object):

	def __init__(self, car_name = "General", car_model = "GM", car_type = "saloon"):
		
		self.model = car_model
		self.name = car_name
		self.type = car_type
		self.speed = 0
		self.num_of_doors = 0
		self.num_of_wheels = 0

		if(self.name == "Porshe" or self.name == "Koenigsegg"):
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if(self.type == "saloon"):
			self.num_of_wheels = 4
		else:
			self.num_of_wheels = 8

	def is_saloon(self):
		if (self.type == "saloon"):
			return  True
		else:
			return False

	def drive(self, moving_speed):
		
		if(moving_speed == 7):
			self.speed = 77
		elif(moving_speed == 3):
			self.speed = 1000

		return self

man = Car('MAN', 'Truck', 'trailer')

print man.speed
print man.type
print man.drive(7).speed