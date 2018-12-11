from input import tree
from collections.abc import Iterable

test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def parse_(tree):
	children, metadata = [tree.pop(0) for _ in range(2)]
	data = []
	data.extend([parse_(tree) for _ in range(children)])
	return data + [tree.pop(0) for _ in range(metadata)]

def flatten(lists):
	for l in lists:
		if isinstance(l, Iterable) and not isinstance(l, (str, bytes)):
			yield from flatten(l)
		else:
			yield l

def partOne(tree):
	return sum(flatten(parse_(tree)))

print(partOne(tree))
