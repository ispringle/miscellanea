from input import initial

test = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

def parse_(input):
	row_buffer = [' ' for char in input.splitlines()[0]]
	row_buffer.append(' ')
	row_buffer.append(' ')
	land = [row_buffer]
	for line in input.splitlines():
		row = [' ']
		for char in line:
			row.append(char)
		row.append(' ')
		land.append(row)
	land.append(row_buffer)
	return land

def printMap(land):
	for row in land:
		print(''.join(row))

def increment(land):
	forest = '|'
	clearing = '.'
	lumberyard = '#'
	_buffer = ' '
	next_minute = []
	y = 0
	for row in land:
		x = 0
		next_row = []
		for acre in row:
			if acre is clearing:
				adj = countSurrounding(land, [x,y])
				if adj[forest] >= 3:
					next_row.append(forest)
				else:
					next_row.append(acre)
			elif acre is forest:
				adj = countSurrounding(land, [x,y])
				if adj[lumberyard] >= 3:
					next_row.append(lumberyard)
				else:
					next_row.append(acre)
			elif acre is lumberyard:
				adj = countSurrounding(land, [x,y])
				if adj[forest] >= 1 and adj[lumberyard] >= 1:
					next_row.append(lumberyard)
				else:
					next_row.append(clearing)
			elif acre is _buffer:
				next_row.append(' ')
			x += 1
		y += 1
		next_minute.append(next_row)
	return next_minute

def countSurrounding(land, acre):
	x, y = acre
	forest = '|'
	clearing = '.'
	lumberyard = '#'
	_buffer = ' '
	count = {forest : 0, clearing : 0, lumberyard : 0, _buffer : 0}
	surroundings = [[x-1, y-1], [x  , y-1], [x+1, y-1],
					[x-1, y  ],             [x+1, y  ],
					[x-1, y+1], [x  , y+1], [x+1, y+1]]
	for loc in surroundings:
		x, y = loc
		count[land[y][x]] += 1
	return count

def countResources(land):
	forest = '|'
	clearing = '.'
	lumberyard = '#'
	_buffer = ' '
	count = {forest : 0, clearing : 0, lumberyard : 0, _buffer : 0}
	for row in land:
		for acre in row:
			count[acre] += 1
	return count

def partOne(land):
	count = 10
	for minute in range(count):
		land = increment(land)
	totals = countResources(land)
	return totals['#'] * totals['|']

def partTwo(land):
	count = 1000000000
	for minute in range(count):
		land = increment(land)
	totals = countResources(land)
	return totals['#'] * totals['|']
#print(countSurrounding(parse_(test), [9,2]))
print(partOne(parse_(initial)))
print(partTwo(parse_(initial)))
