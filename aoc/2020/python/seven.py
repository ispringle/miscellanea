from collections import Counter


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return {
            (splt := line.split(" contain "))[0]: {
                inner[2:]: int(inner[0]) for inner in splt[1].strip().replace(
                    ".", "").split(", ") if inner != "no other"
            }
            for line in open(input_file).read().replace(
                " bags", "").replace(" bag", "").splitlines()
        }

    def part_one(self):
        prev = set(["shiny gold"])
        bags = set()
        data = self.input
        while len(prev) > 0:
            prev = set(
                bag for bag in data for pbag in prev if pbag in data[bag])
            bags |= prev
        return len(bags)

    def part_two(self):
        prev = {"shiny gold": 1}
        total = 0
        data = self.input
        while len(prev) > 0:
            total += sum(sum(
                data[pbag][bag] for bag in data[pbag])
                         * prev[pbag] for pbag in prev)
            prev = sum((
                Counter(
                    {
                        bag: prev[pbag] * data[pbag][bag]
                        for bag in data[pbag]
                    }) for pbag in prev),
                Counter())
        return total

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
