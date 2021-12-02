class Solver:
    def __init__(self, input_file):
        self.timestamp, self.buses, self.total = self.parse(input_file)

    def parse(self, input_file):
        data = open(input_file)
        ts = int(data.readline())
        raw_buses = data.readline().split(',')
        buses = [int(x) for x in raw_buses if x.isnumeric()]
        return ts, buses, len(raw_buses)

    def part_one(self):
        stops = [bus - self.timestamp % bus for bus in self.buses]
        nearest = min(stops)
        return nearest * self.buses[stops.index(nearest)]

    # there has to be a better way
    def part_two(self):
        ts, step = 1, 0
        for bus in self.buses:
            while ts % bus != 0:
                ts += step
            step *= bus
            ts += 1
        return ts - self.total

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
