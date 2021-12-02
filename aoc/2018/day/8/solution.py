from input import tree
from collections.abc import Iterable

test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def partOne(tree):
	children, metadata = [tree.pop(0) for _ in range(2)]
	data = []
	data.extend([partOne(tree) for _ in range(children)])
	return data + [tree.pop(0) for _ in range(metadata)]

def flatten(lists):
	for l in lists:
		if isinstance(l, Iterable) and not isinstance(l, (str, bytes)):
			yield from flatten(l)
		else:
			yield l

def partTwo(tree):
	children, metas = tree[:2]
	data = tree[2:]
	values = []
	for child in range(children):
		value, data = partTwo(data)
		values.append(value)
	if children == 0: return (sum(data[:metas]), data[metas:])
	else:
		return (sum(values[i - 1] for i in data[:metas] if i > 0 and i <= len(values)), data[metas:])

value, _ = partTwo(tree)

print(sum(flatten(partOne(tree))))
print(value)
