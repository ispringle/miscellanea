from collections import defaultdict


class Solver:
    def __init__(self, input_file):
        self.rules, self.mine, self.others = self.parse(input_file)

    def parse(self, input_file):
        rules, mine, others = open(input_file).read().split('\n\n')
        rules = {
            (a := x.split(": "))[0]: list(
                (c := [list(range(int((b := y.split("-"))[0]),
                                  int(b[1]) + 1))
                       for y in a[1].split(" or ")])[0] + c[1])
            for x in rules.splitlines()}
        mine = [int(x) for x in mine.splitlines()[1].split(",")]
        others = [[int(a) for a in x.split(",")]
                  for x in others.splitlines()[1:]]
        return rules, mine, others

    def part_one(self):
        return sum(
            y for x in self.others for y in x if not self.valid_field(y))

    def part_two(self):
        valid = [x for x in self.others if self.valid_ticket(x)]
        potential = defaultdict(set)
        for i in range(len(self.rules)):
            for field, ranges in self.rules.items():
                if all(t[i] in ranges for t in valid):
                    potential[field].add(i)
        departures = 1
        correct = dict()
        for field in sorted(potential, key=lambda x: len(potential[x])):
            for i in potential[field]:
                if i not in correct.values():
                    correct[field] = i
                    if 'depart' in field:
                        departures *= self.mine[i]
        return departures

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")

    def valid_field(self, field):
        return any(field in r for r in self.rules.values())

    def valid_ticket(self, ticket):
        return all(self.valid_field(x) for x in ticket)
