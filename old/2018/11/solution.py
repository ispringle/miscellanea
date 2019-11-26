def powerLevel(x, y):
	gsn = 2568
	#gsn = 18
	rackID = x + 10
	power = rackID * y
	power += gsn
	power *= rackID
	power = int(power / 100)
	return power % 10 - 5

def squarePower(x, y, s):
	return sum([sum([powerLevel(i, j) for j in range(y, y + s)]) for i in range(x, x + s)])

def partOne(size):
	grid = {(x,y):squarePower(x, y, 3) for x in range(1, size - 1) for y in range(1, size - 1)}
	return max(grid, key=lambda key: grid[key])

def partTwo(size):
	grid = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
	grid = [[powerLevel(x, y) for x in range(len(grid))] for y in range(len(grid))]
	for x in range(1, size + 1):
		for y in range(1, size + 1):
			grid[x][y] = grid[x][y] + grid[x-1][y] + grid[x][y-1] - grid[x-1][y-1]
	best = (0, (0, 0))
	for s in range(1, size):
		for x in range(1, size - s + 1):
			for y in range(1, size - s + 1):
				total = grid[x + s][y + s] - grid[x][y + s] - grid[x + s][y] + grid[x][y]
				best = max(best, (total, (x +1, y+1, s)))
	return best[1]



print(partOne(300))
print(partTwo(300))
