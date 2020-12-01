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
        if s := self.part_two() != None:  # Noqa E203
            print(f"Part Two: {self.part_two()}")
