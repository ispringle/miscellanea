class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return {int((a := x.split("\n"))[0].strip("Tile ").strip(":")): a[1:]
                for x in open(input_file).read().split("\n\n")}

    def part_one(self):
        return self.input

    def part_two(self):
        return None

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
