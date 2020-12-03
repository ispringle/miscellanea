class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        with open(input_file, 'r') as f:
            data = f.read()
            self.width = data.find('\n')
            data = data.replace('\n', '')
            self.height = int(len(data) / self.width)
        return data

    def part_one(self):
        return self.count_trees([3, 1])

    def part_two(self):
        slopes = [
            [1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2],
        ]
        product = 1
        for slope in slopes:
            product *= self.count_trees(slope)
        return product

    def count_trees(self, slope):
        x, y = 0, 0
        trees = 0
        while y < self.height:
            obj = self.value_at(x, y)
            if obj == "#":
                trees += 1
            x += slope[0]
            y += slope[1]
        return trees

    def idx(self, x, y):
        x -= int(x / self.width) * self.width
        y *= self.width
        return x + y

    def value_at(self, x, y):
        return self.input[self.idx(x, y)]

    def solve(self):
        print(f"Part One: {self.part_one()}")
        if s := self.part_two() != None:  # Noqa E203
            print(f"Part Two: {self.part_two()}")
