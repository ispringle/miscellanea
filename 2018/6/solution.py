from collections import defaultdict
from collections import Counter
from input import coords

def distance(x, y, ix, iy):
	return abs(x - ix) + abs(y - iy)

#def distances(x, y):],
	#return [distance(x, y, i[0], i[1]) for i in coords]

def ranges(coord):
	r = {}
	for ix in range(edges[2],edges[0]):
		for iy in range(edges[3], edges[1]):
			d = distance(coord[0], coord[1], ix, iy)
			r[ix,iy] = d
	return r

edges = [	#left, upper, right, lower
			max(coord[0] for coord in coords),
			max(coord[1] for coord in coords),
			min(coord[0] for coord in coords),
			min(coord[1] for coord in coords)
]

def partOne(coords):
	#distances = {(coord[0], coord[1]): ranges(coord) for coord in coords}
	distances = {}
	for x in range(edges[2], edges[0]):
		for y in range(edges[3], edges[1]):
			distances[x, y] = {(coord[0], coord[1]): distance(coord[0], coord[1], x, y) for coord in coords}
	map_ = defaultdict(lambda:-1)
	grid = {}
	for coord in distances.keys():
		for loc in distances[coord].keys():
			dist = distances[coord][loc]
			if map_[coord] > dist or map_[coord] == -1:
				map_[coord] = dist
				grid[coord] = loc
			elif map_[coord] == dist:
				grid[coord] += loc
	c = Counter({(coord[0], coord[1]): 0 for coord in coords})
	for coord in grid.keys():
		if grid[coord] in c.keys():
			c[grid[coord]] += 1
	return c.most_common()[0]

ans = partOne(coords)
print(ans)
