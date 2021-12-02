"""
Future-self will need this solution explained:

This input and explanation (BSP) is literally just two binary numbers.
And then they make it even easier for us because the answer is an ID which
is the first binary number, moved 8 bits, and then added to the second
binary number -- which is the same as just sticking the second binary
number behind the first one. And thus 0101100 (44) + 101 (5) is the same
as 0101100101.

The second is just a matter of finding the only seat in the list that
isn't on any of the boarding passes.
"""


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return {int(x.translate(str.maketrans("FBLR", "0101")), 2)
                for x in open(input_file)}

    def part_one(self):
        return max(self.input)

    def part_two(self):
        return max(set(range(max(self.input))) - self.input)

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
