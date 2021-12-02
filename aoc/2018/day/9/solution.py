from input import conditions
from collections import deque, defaultdict

conditions = conditions.split()
players = int(conditions[0])
last_marble = int(conditions[-2])

def wantToPlayAGame(players, last_marble):
	scores = defaultdict(int)
	circle = deque()
	partOne = 0
	for marble in range(1, (last_marble + 1)):
			if marble % 23 == 0:
				circle.rotate(7)
				scores[marble % players] += marble + circle.pop()
				circle.rotate(-1)
			else:
				circle.rotate(-1)
				circle.append(marble)
	partOne = max(scores.values())
	for marble in range(last_marble + 1, (last_marble * 100 + 1)):
			if marble % 23 == 0:
				circle.rotate(7)
				scores[marble % players] += marble + circle.pop()
				circle.rotate(-1)
			else:
				circle.rotate(-1)
				circle.append(marble)
	return partOne, max(scores.values())

scores = wantToPlayAGame(players, last_marble)
print(f"With {last_marble} marbles the winning score is {scores[0]}.")
print(f"With {last_marble * 100} marbles the winning score is {scores[1]}")

