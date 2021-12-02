from input import input
from collections import Counter

def partOne(ids):
	twos = 0
	threes = 0
	for id in ids:
		two, three = tallyChars(id)
		twos += two
		threes += three
	return twos * threes

def tallyChars(id):
	counts = Counter()
	twos = 0
	threes = 0
	for char in id:
		counts[char] += 1
	for count in counts:
		if counts[count] == 2:
			twos = 1
		if counts[count] == 3:
			threes = 1
	return twos, threes

def partTwo(ids):
	for id in ids:
		for altID in ids:
			diff = 0
			d_char = 0
			loc = -1
			for i,j in zip(id, altID):
				loc += 1
				if diff > 1:
					break
				if i != j:
					diff += 1
					d_char = loc
			if diff == 1:
				return id[:d_char] + id [d_char + 1:]

checksum = partOne(input)
match = partTwo(input)

print("The checksum is " + str(checksum)
		+ " and the matching ids are '"
		+ match + "'.")
