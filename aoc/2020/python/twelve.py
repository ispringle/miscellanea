"""
Dear Furute Self,

Read this:
https://en.wikipedia.org/wiki/Rotation_matrix

Sincerly,
Present Self
"""

from math import sin, cos, radians


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)
        self.dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

    def parse(self, input_file):
        return [(x[0], int(x[1:])) for x in open(input_file).readlines()]

    def part_one(self):
        x, y, a = 0, 0, 90
        for step, n in self.input:
            if step in self.dirs:
                dx, dy = self.dirs[step]
                x += n * dx
                y += n * dy
            elif step in ['L', 'R']:
                a += n if step == 'R' else 360 - n
                a %= 360
            elif step == 'F':
                theta = radians(a)
                y += int(cos(theta) * n)
                x += int(sin(theta) * n)
        return abs(x) + abs(y)

    def part_two(self):
        x, y, x_way, y_way = 0, 0, 10, 1
        for step, n in self.input:
            if step in self.dirs:
                dx, dy = self.dirs[step]
                x_way += n * dx
                y_way += n * dy
            elif step in {'L', 'R'}:
                a = n if step == 'R' else 360 - n
                if a == 90 or a == 270:
                    t = y_way
                    y_way = x_way * (-1 if a == 90 else 1)
                    x_way = t * (1 if a == 90 else -1)
                elif a == 180:
                    x_way *= -1
                    y_way *= -1
            elif step == 'F':
                x += n * x_way
                y += n * y_way
        return abs(x) + abs(y)

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
