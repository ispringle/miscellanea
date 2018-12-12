from input import initial_state, observations

def countPlants(pots):
	d = (len(pots) - 100) //2
	s = 0
	for n, pot in enumerate(pots):
		if pot == '#':
			s += (n - diff)
	return s

c_gen = initial_state
p_count = countPlants(initial_state)
differences = []
generations = 1000
gg = 50000000000

for i in range(generations):
	if i == 20:
		print(f"There are {countPlants(c_gen)} after 20 generations")
	c_gen = "."*4 + c_gen + "."*4
	n_gen = ''
	for n in range(2, len(c_gen) - 2):
		state = c_gen[n-2:n+3]
		n_gen += observations[state]
	c_gen = n_gen
	c_count = countPlants(c_gen)
	differences.append(c_count - p_count)
	p_count = c_count
	if len(differences) > 100:
			differences.pop(0)
ld = sum(differences) // len(differences)
total = (gg - generations) * ld + countPlants(c_gen)
print(f"After {gg} generations there will be {total} plants.")
