from collections import Counter


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        data = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                l = line.split()
                m, x = l[0].split("-")
                c = l[1].strip(":")[0]
                data.append([int(m), int(x), c, l[-1]])
        return data

    def part_one(self):
        correct = 0
        for item in self.input:
            m, x, c, p = item
            p = Counter(p)
            if c in p:
                if p[c] >= m and p[c] <= x:
                    correct += 1
        return correct

    def part_two(self):
        correct = 0
        for item in self.input:
            m, x, c, p = item
            c1 = p[m-1]
            c2 = p[x-1]
            if c1 != c2:
                if c1 == c or c2 == c:
                    correct += 1
        return correct

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s != None:  # Noqa E203
            print(f"Part Two: {s}")
