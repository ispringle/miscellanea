class Intcomp:
    def __init__(self, intcode):
        self.intcode = intcode
        self.curr_pos = 0
        self.curr_optcode = intcode[self.curr_pos]

    def set_input(self, noun, verb):
        self.intcode[1] = noun
        self.intcode[2] = verb

    def run(self):
        while self.curr_optcode != 99:
            if self.curr_optcode == 1:
                self.add()
            elif self.curr_optcode == 2:
                self.multiply()
            self.curr_pos += 4
            self.curr_optcode = self.intcode[self.curr_pos]

    def add(self):
        pos_x = self.intcode[self.curr_pos + 1]
        pos_y = self.intcode[self.curr_pos + 2]
        pos_z = self.intcode[self.curr_pos + 3]
        self.intcode[pos_z] = self.intcode[pos_x] + self.intcode[pos_y]

    def multiply(self):
        pos_x = self.intcode[self.curr_pos + 1]
        pos_y = self.intcode[self.curr_pos + 2]
        pos_z = self.intcode[self.curr_pos + 3]
        self.intcode[pos_z] = self.intcode[pos_x] * self.intcode[pos_y]


def solve_a(puzzle):
    intcomp = Intcomp(puzzle)
    intcomp.set_input(12, 2)
    intcomp.run()
    return intcomp.intcode[0]


def solve_b(puzzle):
    pos_zero = 0
    for noun in range(100):
        for verb in range(100):
            intcomp = Intcomp(puzzle)
            intcomp.set_input(noun, verb)
            intcomp.run()
            if intcomp.intcode[0] == 19690720:
                return (100 * noun) + verb


def solve(puzzle):
    puzzle = clean_input(puzzle)
    a = solve_a(puzzle)
    b = solve_b(puzzle)
    return (a, b)


def clean_input(puzzle):
    return [int(x) for x in puzzle.split(',')]


def test(puzzle):
    puzzle = clean_input(puzzle)
    intcomp = Intcomp(puzzle)
    intcomp.run()
    return intcomp.intcode[0]


if __name__ == "__main__":
    import sys
    #print(test(sys.argv[1]))
