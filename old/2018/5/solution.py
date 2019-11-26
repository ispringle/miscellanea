from input import polymer
import string

def react(polymer):
	unit = 0
	while unit < (len(polymer) - 1):
		if polymer[unit] != polymer[unit+1] and polymer[unit].lower() == polymer[unit+1].lower():
			polymer = polymer[:unit]+polymer[unit+2:]
			unit = max(0, unit-1)
		else:
			unit += 1
	return polymer

def partOne(polymer):
	return len(react(polymer))

def partTwo(polymer):
	optimized = len(polymer)
	for char in string.ascii_lowercase:
		test_polymer = polymer.replace(char, "").replace(char.upper(), "")
		optimized = min(optimized, len(react(test_polymer)))
	return optimized

print(partOne(polymer))
print(partTwo(polymer))

	
