from input import instructions

def parse_(instructions):
	inst = {}
	return [[i.split()[1], i.split()[7]] for i in instructions]

def next_(valid):
	if len(valid) > 0:
		return sorted(valid)[0]

def purge(instructions, purged):
	return [i for i in instructions if i[0] != purged]

def partOne(instructions):
	instructions = parse_(instructions)
	valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	last = set([i[1] for i in instructions if i[1] not in [j[0] for j in instructions]])
	ordered = ''
	while len(valid) > 0:
		n = next_(valid)
		ordered += n
		instructions = purge(instructions, n)
		valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	ordered += next_(last)
	return ordered

def partTwo(instructions):
	alphabet = sorted(list("qwertyuiopasdfghjklzxcvbnm"))
	elf_count = 5
	time_mod = 60
	times = {alpha: sec + 1 + time_mod for sec, alpha in enumerate(alphabet)}
	instructions = parse_(instructions)
	valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	last = set([i[1] for i in instructions if i[1] not in [j[0] for j in instructions]])
	ordered = ''
	working = []
	total = 0
	while len(valid) > 0:
		for elf in range(elf_count):
			n = next_([i for i in list(valid) if i not in [j[0] for j in working]])
			if len(working) < elf_count and n not in [i[0] for i in working] and n is not None:
				working.append([n, times[n.lower()]])
		completed = ['letter',10000]
		for elf in working:
			if elf[1] < completed[1]:
				completed[0] = elf[0]
				completed[1] = elf[1]
		for elf in working:
			elf[1] -= completed[1]
		total += completed[1]
		fin = completed[0]
		instructions = purge(instructions, fin)
		valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
		del working[working.index([i for i in working if fin in i][0])]
	total += times[next_(last).lower()]
	return total

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
print(partTwo(instructions))
