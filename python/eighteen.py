import re


class NewInt(int):
    def __mul__(self, other):
        return NewInt(int(self) * other)

    def __pow__(self, other):
        return NewInt(int(self) + other)

    def __truediv__(self, other):
        return NewInt(int(self) + other)


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def eval(self, expression, switch_op):
        return eval(re.sub(r"(\d+)", r"NewInt(\1)",
                           expression.replace("+", switch_op)))

    def parse(self, input_file):
        return open(input_file).readlines()

    def part_one(self):
        return sum(self.eval(expression, "/") for expression in self.input)

    def part_two(self):
        return sum(self.eval(expression, "**") for expression in self.input)

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
