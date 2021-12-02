class Solver:
    def __init__(self, input_file):
        self.raw_rules, self.messages = self.parse(input_file)

    def check(self, message, part):
        if message == '' or part == []:
            return message == '' and part == []
        rule = self.rules[part[0]]
        if '"' in rule:
            if message[0] in rule:
                return self.check(message[1:], part[1:])
            else:
                return False
        else:
            return any(self.check(message, x + part[1:]) for x in rule)

    def parse(self, input_file):
        raw_rules, messages = [x.splitlines()
                               for x in open(input_file).read().split("\n\n")]
        return raw_rules, messages

    def parse_rules(self, rules):
        def __parse(rule):
            number, match = rule.split(":")
            if '"' not in match:
                match = [[int(x) for x in y.split()]
                         for y in match.split("|")]
            return (int(number), match)
        return {(a := __parse(r))[0]: a[1] for r in rules}

    def part_one(self):
        self.rules = self.parse_rules(self.raw_rules)
        return sum(self.check(message, [0]) for message in self.messages)

    def part_two(self):
        self.rules = self.parse_rules(self.raw_rules +
                                      ["8: 42 | 42 8", "11: 42 31 | 42 11 31"])
        return sum(self.check(message, [0]) for message in self.messages)

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
