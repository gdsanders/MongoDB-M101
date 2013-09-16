fruit = ['orange', 'banana', 'kiwi', 'orange', 'banana', 'apple']

# number of fruit in array

def analyze_list(l):
	
	counts = {}
	for item in l:
		if item in counts:
			counts[item] = counts[item] + 1
		else:
			counts[item] = 1

	return counts

	# let's analyze the list

counts = analyze_list(fruit)
print counts

