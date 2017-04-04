# function to find the missing number

def find_missing(l1, l2):
	sum_l1 = sum(l1)
	sum_l2 = sum(l2)
	if (sum_l1 > sum_l2):
		return sum_l1 - sum_l2
	else:
		return sum_l2 - sum_l1

print (find_missing([4, 6, 8], [4, 6, 8, 10]))
