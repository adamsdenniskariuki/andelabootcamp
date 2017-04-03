# funtion to calculate prime numbers

def gen_prime(n):

	"""
		Steps: Validate input, loop through the numbers in the range, save
		the numbers in a list and output the list of prime numbers.

		Asymptotic Analysis is O(N^2) because of the 2 for loops and each element is looped over twice
		in order to complete the calculation

	"""

	if (n == ""):
		return "Input cannot be empty"
	elif (n < 0):
		return "Input cannot be negative"
	elif (isinstance(n, int) == False):
		return "Input must be an integer"
	else:

		out = []
		is_prime = 1
		
		for i in range(2, n + 1):
			
			for j in range(2, i):
				
				if ((i % j) == 0):
					is_prime = 0
					break

			if(is_prime == 1):
				out.append(i)

			is_prime = 1

	return out

print gen_prime(83)

