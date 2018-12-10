from input import tree

def parse_(tree, metadata):
	if len(tree) > 0:
		#print(f"Tree: {tree}")
		nodes = tree[0]
		meta = tree[1]
		if tree[0] < 1:
			#print(f"Metadata: {tree[2:2 + meta]}")
			metadata.append(tree[2: 2 + meta])
			parse_(tree[2+meta:], metadata)
		else: 
			#print(f"Metadata: {tree[-meta:]}")
			metadata.append(tree[-meta:])
			parse_(tree[2:-meta], metadata)
	return metadata

def partOne(tree):
	metadata = parse_(tree, [])
	sum = 0
	for packet in metadata:
		for data in packet:
			sum += data
	return sum

test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
print(partOne(test))

