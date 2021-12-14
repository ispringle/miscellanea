from collections import defaultdict

network = defaultdict(list)
for line in open("input.txt"):
    frm, to = line.strip().split("-")
    network[frm] += [to]
    network[to] += [frm]


def travel(cave="start", visited=[], smallTwice=True):
    if cave == "end":
        return 1
    if cave in visited:
        if cave == "start":
            return 0
        if cave.islower():
            if smallTwice:
                return 0
            else:
                smallTwice = True
    acc = 0
    for nxt in network[cave]:
        acc += travel(nxt, visited + [cave], smallTwice)
    return acc


print(travel(smallTwice=True))
print(travel(smallTwice=False))
