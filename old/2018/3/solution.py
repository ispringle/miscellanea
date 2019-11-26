from input import input
from collections import defaultdict

claims = input

def createFabric(claims):
	fabric = defaultdict(int)
	for id, x, y, w, h in claims:
		for i in range(w):
			for j in range(h):
				fabric[(i+x, j+y)] += 1
	return fabric

def partOne(claims):
	fabric = createFabric(claims)
	tally = 0
	for i in fabric.values():
		if i > 1:
			tally += 1
	return fabric, tally

def partTwo(fabric, claims):
	for id, x, y, w, h in claims:
		found = True
		for i in range(w):
			for j in range(h):
				if fabric[(i+x, j+y)] != 1:
					found = False
					break
			if not found:
				break
		if found:
			return id

fabric, tally = partOne(claims)
id = partTwo(fabric, claims)
print("There is " + str(tally)
		+ " square inches of overlapping claims.\n"
		+ "The only claim that doesn't overlap is "
		+ str(id) + ".")
