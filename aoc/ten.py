from collections import Counter


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)
        self.input.append(self.input[-1] + 3)

    def parse(self, input_file):
        return sorted([int(x) for x in open(input_file).readlines()])

    def part_one(self):
        joltage = 0
        diffs = [0, 0, 0, 0]
        for n in self.input:
            if (i := n - joltage) <= 3:
                joltage = n
                diffs[i] += 1
        return diffs[1] * diffs[3]

    def part_two(self):
        c = Counter([0])
        for j in self.input:
            c[j] = c[j - 1] + c[j - 2] + c[j - 3]
        return c[self.input[-1]]

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
