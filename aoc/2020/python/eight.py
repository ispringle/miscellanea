from copy import deepcopy


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [[(a := x.split())[0], int(a[1])]
                for x in open(input_file).readlines()]

    def part_one(self):
        return self.run(self.input)[0]

    def part_two(self):
        d = self.input
        for i in reversed(range(len(d))):
            if d[i][1] == "acc":
                continue
            inst = "jmp" if d[i][0] == "nop" else "nop"
            new = deepcopy(d)
            new[i][0] = inst
            if (s := self.run(new))[1]:
                return s[0]

    def run(self, prg):
        a, i = 0, 0
        v = [False for _ in range(len(prg))]
        while True:
            if i == len(prg):
                return (a, True)
            elif v[i]:
                return (a, False)
            else:
                v[i] = True
            inst, num = prg[i]
            if inst == "acc":
                a += num
            elif inst == "jmp":
                i += num - 1
            i += 1

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
