from input import nodes
from queue import PriorityQueue

#Part 1
longest = max(nodes.keys())
lc = nodes[longest]
ranges = {i:sum([abs(j[0] - lc[0]), abs(j[1] - lc[1]), abs(j[2] - lc[2])])
					for i,j in nodes.items()}
within_range = [i for i,j in ranges.items() if j <= longest]

#Part 2
q = PriorityQueue()
for r, c in nodes.items():
	d = abs(c[0]) + abs(c[1]) + abs(c[2])
	q.put((max(0, d - r), 1))
	q.put((d + r, -1))
c, mc, r = [0]*3
while not q.empty():
	d, e = q.get()
	c += e
	if c > mc: r, mc = d, c

print(f"There are {len(within_range)} nodes in range.")
print(f"The distance from zero to the most common coord is {r}.")

