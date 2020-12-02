from collections import Counter
import re


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        data = [re.split("[: \-]", line) for line in open(input_file)]  # Noqa: W605, E501
        return [[int(a), int(b), c, d] for a, b, c, _, d in data]

    def part_one(self):
        correct = 0
        for item in self.input:
            m, x, c, p = item
            p = Counter(p)
            if c in p:
                if p[c] >= m and p[c] <= x:
                    correct += 1
        return correct

    def part_two(self):
        correct = 0
        for item in self.input:
            m, x, c, p = item
            c1 = p[m-1]
            c2 = p[x-1]
            if c1 != c2:
                if c1 == c or c2 == c:
                    correct += 1
        return correct

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s != None:  # Noqa E203
            print(f"Part Two: {s}")
