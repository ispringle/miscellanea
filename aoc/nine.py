from itertools import product


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [int(x) for x in open(input_file).readlines()]

    def part_one(self):
        prior = self.input[:25]
        for n in self.input[25:]:
            found = False
            for x, y in product(prior, repeat=2):
                if x + y == n:
                    found = True
                    break
            if not found:
                self.target = n
                return n
            prior = prior[1:] + [n]

    def part_two(self):
        low = 0
        for hi in range(len(self.input)):
            while low <= hi and sum(self.input[low:hi]) > self.target:
                low += 1
            if sum(self.input[low:hi]) == self.target:
                return min(self.input[low:hi]) + max(self.input[low:hi])

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
