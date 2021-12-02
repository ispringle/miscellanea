class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        with open(input_file, 'r') as f:
            data = f.readlines()
        return data

    def part_one(self):
        return 0

    def part_two(self):
        return None

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
