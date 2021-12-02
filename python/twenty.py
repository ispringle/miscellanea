class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        def sides(piece):
            t = str.maketrans(".#", "01")
            top = int(piece[0].translate(t), 2)
            bottom = int(piece[-1].translate(t), 2)
            left = int(''.join(x[0] for x in piece).translate(t), 2)
            right = int(''.join(x[-1] for x in piece).translate(t), 2)
            return top, bottom, left, right

        return {int((a := x.split("\n"))[0].strip("Tile ").strip(":")):
                sides(a[1:])
                for x in open(input_file).read().split("\n\n")
                if x}

    def part_one(self):
        return self.input

    def part_two(self):
        return None

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
