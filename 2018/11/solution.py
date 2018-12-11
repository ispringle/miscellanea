def powerLevel(x, y):
	gsn = 2568
	rackID = x + 10
	power = rackID * y
	power += gsn
	power *= rackID
	power = int(power / 100)
	return power % 10 - 5

def squarePower(x, y):
	return sum([sum([powerLevel(i, j) for j in range(y, y + 3)]) for i in range(x, x + 3)])

def partOne():
	grid = [[squarePower(x, y) for x in range(1, 299)] for y in range(1, 299)]
	loc = []
	best = -100
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] > best:
				best = grid[y][x]
				loc = [x + 1, y + 1]
	return loc

print(partOne())
