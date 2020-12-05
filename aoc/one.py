from itertools import product
from functools import reduce
from operator import mul


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        with open(input_file, 'r') as f:
            data = f.readlines()
        return [int(x.strip()) for x in data]

    def part_one(self):
        i = self.input
        return [reduce(mul, x) for x in product(i, i) if sum(x) == 2020][0]

    def part_two(self):
        i = self.input
        # This is pretty, but slow. :sad_pepe:
        # return [reduce(mul, x) for x in product(i, i, i) if sum(x) == 2020][0]
        # This is fast, but ugly.
        for x in i:
            for y in i:
                for z in i:
                    if x+y+z == 2020:
                        return x*y*z

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
