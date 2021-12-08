class Segment:
    def __init__(self, definitions, wires):
        self.wires = set(wires)
        self.defintions = definitions
        self.kind = None
        kind = [k for k, v in self.defintions.items() if v == self.wires]
        self.kind = kind[0] if kind else None


class Display:
    def __init__(self, raw_definitions, segments):
        self.raw_definitions = raw_definitions.split()
        self.raw_segments = segments
        self.definitions = self.parse_definitions()
        self.segments = self.parse_segments()
        self.output = int(''.join(str(x.kind) for x in self.segments))

    def parse_definitions(self):
        one = set([x for x in self.raw_definitions if len(x) == 2][0])
        four = set([x for x in self.raw_definitions if len(x) == 4][0])
        seven = set([x for x in self.raw_definitions if len(x) == 3][0])
        eight = set([x for x in self.raw_definitions if len(x) == 7][0])
        nine = set([x for x in self.raw_definitions if len(x)
                   == 6 and len(four - set(x)) == 0][0])
        zero = set([x for x in self.raw_definitions if len(x)
                    == 6 and set(x) != nine and len(one - set(x)) == 0][0])
        six = set([x for x in self.raw_definitions if len(x)
                   == 6 and set(x) != nine and set(x) != zero][0])
        three = set([x for x in self.raw_definitions if len(x) == 5 and len(
            set(x) - nine) == 0 and len(one - set(x)) == 0][0])
        five = set([x for x in self.raw_definitions if len(x)
                    == 5 and len(six - set(x)) == 1][0])
        two = set([x for x in self.raw_definitions if len(x)
                   == 5 and set(x) != five and set(x) != three][0])
        return {1: one, 2: two, 3: three, 4: four, 5: five,
                6: six, 7: seven, 8: eight, 9: nine, 0: zero}

    def parse_segments(self):
        segments = []
        for segment in self.raw_segments.split():
            segments.append(Segment(self.definitions, segment))
        return segments

    def count_segment_kinds(self):
        counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}
        for segment in self.segments:
            if segment.kind:
                counter[segment.kind] += 1
        return counter


def main(file_name):
    input = [*open(file_name)]
    displays = []
    for line in input:
        displays.append(Display((l := line.split(" | "))[0], l[1]))
    print("Part 1: ", sum([v for x in displays for k,
          v in x.count_segment_kinds().items() if k in [1, 4, 7, 8]]))
    print("Part 2: ", sum([x.output for x in displays]))


if __name__ == "__main__":
    main('input.txt')
    # main('test.txt')
