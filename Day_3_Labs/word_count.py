def words(word):

	list_of_words = [int(i) if i.isdigit() else i for i in word.split()]
	list_of__unique_words = list(set(list_of_words))
	out = {}

	for u in list_of__unique_words:
		count = 0
		for w in list_of_words:
			if (w == u):
				count += 1
		out[u] = count 

	return out

print (words("testing 1\t2 testing"))