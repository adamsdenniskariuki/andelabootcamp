#class for binary search

class BinarySearch(list):

	def __init__(self, a, b):
		self.a = a
		self.b = b

		for i in range(self.b - 1, self.a * self.b, self.b):
			list.append(self, i + 1)

		self.length = len(list(self))

	def search(self, value):
		count = 0
		index = 0
		start = 0
		end = self.length

		while start < end:

			count += 1
			
			index = (end + start) // 2

			if(value == list(self)[index]):
				return {'count' : count, 'index' : index}
			else:
				if(value > list(self)[index]):
					if(start == index):
						return {'count' : count - 2, 'index' : -1}
					start = index
				else:
					if(end == index):
						return {'count' : count - 2, 'index' : -1}
					end = index

one_to_twenty = BinarySearch(20, 2)

print(one_to_twenty[0])
print(one_to_twenty.length)
print(one_to_twenty.search(40))



