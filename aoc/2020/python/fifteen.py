class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [int(x) for x in open(input_file).read().split(',')]

    def part_one(self):
        return self.play(2020)

    def part_two(self):
        return self.play(30000000)

    def play(self, rounds):
        spoken = {y: x+1 for x, y in enumerate(self.input)}
        turn, n_xt, last = len(self.input) + 1, 0, 0
        while True:
            if turn == rounds:
                return last
            elif last in spoken:
                n_xt = turn - spoken[last]
                spoken[last] = turn
                last = n_xt
            else:
                spoken[last] = turn
                last = 0
            turn += 1

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
