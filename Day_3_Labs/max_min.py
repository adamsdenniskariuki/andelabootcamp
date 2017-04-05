def find_max_min(l):
	
	l.sort()

	min_num = l[0]
	max_num = l[-1]

	if(min_num == max_num):
		 return [len(l)]
	else:
		return [min_num, max_num] 

print (find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]))
