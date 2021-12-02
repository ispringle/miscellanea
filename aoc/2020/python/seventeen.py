from collections import Counter
from itertools import product


ACTIVE = "#"
INACTIVE = "."


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def increment(self, coord, diff):
        return tuple(a + b for a, b in zip(coord, diff))

    def count(self, dimension, three_dimensions=True):
        xyz_coord = (-1, 0, 1)
        if three_dimensions:
            w_coord = (0,)
        else:
            w_coord = xyz_coord
        new_state = Counter(
            self.increment(coord, diff)
            for coord in dimension
            for diff in product(xyz_coord, xyz_coord, xyz_coord, w_coord)
            if diff != (0, 0, 0, 0))
        return {coord: ACTIVE
                for coord, neighbors in new_state.items()
                if neighbors == 3 or
                (neighbors == 2 and coord in dimension)}

    def parse(self, input_file):
        return {(x, y, 0, 0): a
                for y, b in enumerate(open(input_file).readlines())
                for x, a in enumerate(b.strip())
                if a == ACTIVE}

    def part_one(self):
        pbs = self.input
        for _ in range(6):
            pbs = self.count(pbs)
        return len(pbs)

    def part_two(self):
        pbs = self.input
        for _ in range(6):
            pbs = self.count(pbs, three_dimensions=False)
        return len(pbs)

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
