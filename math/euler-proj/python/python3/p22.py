from assets.p022_names import names

names = sorted(names)

def sum_(name):
	alpha = sorted("qwertyuiopasdfghjklzxcvbnm".upper())
	value = 0
	for char in name:
		value += alpha.index(char) + 1
	return value

total = 0
for name in names:
	value = sum_(name)
	total += value * (names.index(name) + 1)
print(total)


