from input import input
from collections import Counter
test = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz',
]
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
			d_char = ''
			for i,j in zip(id, altID):
				if diff > 1:
					break
				if i != j:
					diff += 1
					d_char = j
			if diff == 1:
				return altID.replace(d_char, '')

print(partOne(input))
print(partTwo(input))
