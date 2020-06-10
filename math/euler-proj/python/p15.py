"""
For a square grid of size n, how many possible ways can you go from (0,n) to (n,0)
if you can only travel down and to the right?
Answer for a grid of size 20: 137846528820
"""

gridSize = 20
paths = 1

i = 0
while i < gridSize:
    paths *= (2 * gridSize) - i
    paths /= i + 1
    i += 1
print(paths)
