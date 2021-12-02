from collections import Counter


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        with open(input_file, 'r') as f:
            d = f.read()
        d = [(x.replace('\n', ''), x.count('\n')+1) for x in d.split("\n\n")]
        return d[:-1]

    def part_one(self):
        a = []
        for b in self.input:
            u = set()
            for c in b[0]:
                u.add(c)
            a.append(u)
        return sum([len(x) for x in a])

    def part_two(self):
        a = [(Counter(x[0]), x[1]) for x in self.input]
        count = 0
        for b in a:
            for _, v in b[0].items():
                if v == b[1]:
                    count += 1
        return count

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
