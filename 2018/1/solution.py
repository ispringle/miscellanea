from input import input
import time

def partOne():
	return sum(input)

def partTwoBruteForce():
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

s_one = partOne()
if s_one == 0:
	s_two = 0
else:
	start = time.time()
	s_two = partTwoBruteForce()
	end = time.time()
	total = end - start

print("The frequency of the initial pass is " + str(s_one) 
		+ " and the first repeat frequency is " + str(s_two)
		+ ".\nIt took " + str(total)
		+ " seconds to run part two.")
