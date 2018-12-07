from collections import defaultdict
from input import coords

def distance(x, y, ix, iy):
	return abs(x - ix) + abs(y - iy)

#def distances(x, y):],
	#return [distance(x, y, i[0], i[1]) for i in coords]

def ranges(coord):
	r = defaultdict(int)
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
	distances = {(coord[0], coord[1]): ranges(coord) for coord in coords}

partOne(coords)
