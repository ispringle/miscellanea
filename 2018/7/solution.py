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
	elves = {i: {'e': None, 'w': False, 'i': ''} for i in range(elf_count)}
	times = {alpha: sec + 1 + time_mod for sec, alpha in enumerate(alphabet)}
	instructions = parse_(instructions)
	valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
	last = set([i[1] for i in instructions if i[1] not in [j[0] for j in instructions]])
	ordered = ''
	time = 0
	working = True
	unavailable = []
	while working:
		for elf in elves.keys():
			valid = set([i[0] for i in instructions if i[0] not in [j[1] for j in instructions]])
			valid = [i for i in valid if i not in unavailable]
			if elves[elf]['w']:
				working = True
				if elves[elf]['e'] == time:
					elves[elf]['w'] = False
					ordered += elves[elf]['i']
					instructions = purge(instructions, n)
					del unavailable[unavailable.index(elves[elf]['i'])]
					elves[elf]['i'] = ''
			elif len(valid) > 0:
				n = next_(valid)
				unavailable.append(n)
				elves[elf]['i'] = n
				elves[elf]['e'] = time + times[n.lower()]
				elves[elf]['w'] = True
		working = False
		for elf in elves.keys():
			if elves[elf]['w']:
				working = True
		time += 1
		print(time)
		print(valid)
		print(unavailable)
		print(elves)
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
print(partTwo(instructions))
