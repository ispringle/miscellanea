from input import log
from collections import defaultdict, Counter
import operator

def parse_(log):
	guards = defaultdict(Counter)
	for entry in sorted(log):
		time, action = entry.split('] ')
		minute = int(time[-2:])
		if action.startswith('G'): guard = int(action.split()[1][1:])
		elif action.startswith('f'): start = minute
		elif action.startswith('w'):
			minutes = minute - start
			guards[guard].update(Counter(start+i for i in range(minutes)))
	return guards

def partOne(log):
	guards= parse_(log)
	_, most_tired = max((sum(minute.values()), id) 
							for id, minute in guards.items())
	return (most_tired * guards[most_tired].most_common()[0][0]), guards

def partTwo(guards):
	(_, minute), id = max((minute.most_common()[0][::-1], id) 
							for id, minute in guards.items())
	return id * minute


p1, guards = partOne(log)
p2 = partTwo(guards)

print("The answer to strategy one is " + str(p1) + ".\n"
		+ "The answer to strategy two is " + str(p2) + ".")



