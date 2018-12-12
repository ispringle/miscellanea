#from input import initial_state, observations

"""Test data"""
initial_state = '#..#.#..##......###...###'

observations = {
			'...##' : '#',
			'..#..' : '#',
			'.#...' : '#',
			'.#.#.' : '#',
			'.#.##' : '#',
			'.##..' : '#',
			'.####' : '#',
			'#.#.#' : '#',
			'#.###' : '#',
			'##.#.' : '#',
			'##.##' : '#',
			'###..' : '#',
			'###.#' : '#',
			'####.' : '#'
}

pots = "."*30 + initial_state + "."*300
#initial_state = deque(initial_state.split())

generations = 20
plants = 0
next_gen = [pot for pot in pots]
for gen in range(generations):
	print(pots)
	for i in range(len(pots)-5):
		j = i + 5
		k = i + 2
		if pots[i:j] in observations.keys():
			next_gen[k] = observations[pots[i:j]]
	pots = ''.join(next_gen)

print(plants)

"""
#    #  ###  ### ########
#   #   #  ##  # #
#  #    #  ##  # #
###     #  ##  # ########
#  #    #      #        #
#   #   #      #        #
#    #  #      #        #
#     # #      # ########
"""
