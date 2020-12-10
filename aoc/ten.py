from itertools import product


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [int(x) for x in open(input_file).readlines()]

    def part_one(self):
        joltage, ones, threes = 0, 0, 1
        for n in sorted(self.input):
            if (i := n - joltage) <= 3:
                joltage = n
                if i == 1:
                    ones += 1
                elif i == 3:
                    threes += 1
            else:
                break
        return ones * threes

    def part_two(self):
        return None

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
