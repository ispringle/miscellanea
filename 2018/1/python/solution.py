from input import input

def partOne():
	return sum(input)

def partTwo():
	t_input = tuple(input)
	prev = set([0])
	curr = list(t_input)
	sum = 0
	
	while True:
		try:
			sum += curr.pop(0)
		except:
			curr = list(t_input)
			sum += curr.pop(0)
	
		if sum in prev:
			return sum
		else:
			prev.add(sum)

print(partOne())
print(partTwo())
