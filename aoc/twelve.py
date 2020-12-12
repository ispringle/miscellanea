class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [(x[0], int(x[1:])) for x in open(input_file).readlines()]

    def part_one(self):
        """
        East = +x
        West = -X
        North = +y
        South = -y
        """
        direction, x, y = "E", 0, 0

        def _move(d, mod):
            def __move(n):
                return d + mod * n
            return __move
        move = {
            "E": _move(x, 1),
            "W": _move(x, -1),
            "N": _move(y, 1),
            "S": _move(y, -1),
        }
        for c, n in self.input:
            if c == "F":
                x = move[direction](n)
            if c == "N":
                y = move["N"](n)
            if c == "S":
                y = move["S"](n)
            if c == "E":
                x = move["E"](n)
            if c == "W":
                x = move["W"](n)
        return (x, y)

    def part_two(self):
        return None

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
