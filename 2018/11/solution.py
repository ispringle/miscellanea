def powerLevel(x, y):
	#gsn = 2568
	gsn = 18
	rackID = x + 10
	power = rackID * y
	power += gsn
	power *= rackID
	power = int(power / 100)
	return power % 10 - 5

def squarePower(x, y, s):
	return sum([sum([powerLevel(i, j) for j in range(y, y + s)]) for i in range(x, x + s)])

def partOne():
	grid = [[squarePower(x, y, 3) for x in range(1, 299)] for y in range(1, 299)]
	best = max([max(i) for i in grid])
	#return [[[x+1,y+1] for x in range(len(grid[y])) if grid[y][x] == best] for y in range(len(grid))]
	loc = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == best:
				loc = [x + 1, y + 1]
	return loc

def partTwo():
	best = -1000000
	loc = []
	size = 0
	for s in range(1,300):
		grid = [[squarePower(x, y, 3) for x in range(1, 301 - s)] for y in range(1, 301 - s)]
		for y in range(len(grid)):
			for x in range(len(grid[y])):
				if grid[y][x] > best:
					best = grid[y][x]
					loc = [x + 1, y + 1]
					size = s
	return loc + [size]


print(partOne())
#print(partTwo())
