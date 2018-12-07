from input import instructions

def parse_(instructions):
	inst = {}
	return [[i.split()[1], i.split()[7]] for i in instructions]

def next_(valid):
	return sorted(valid)[0]

def purge(instructions, purged):
	return [i for i in instructions if i[0] != purged]

def partOne(instructions):
	instructions = parse_(instructions)
	valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	last = set([i[1] for i in instructions if i[1] not in [j[0] for j in instructions]])
	ordered = ''
	while len(valid) > 0:
		print(valid)
		n = next_(valid)
		ordered += n
		instructions = purge(instructions, n)
		valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	ordered += next_(last)
	return ordered

test = [
		"Step C must be finished before step A can begin.",
		"Step C must be finished before step F can begin.",
		"Step A must be finished before step B can begin.",
		"Step A must be finished before step D can begin.",
		"Step B must be finished before step E can begin.",
		"Step D must be finished before step E can begin.",
		"Step F must be finished before step E can begin.",
]
print(partOne(instructions))
#print(partOne(test))

