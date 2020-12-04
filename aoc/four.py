import re


class Solver:

    def __init__(self, input_file):
        self.input = self.parse(input_file)
        self.validation = {
            "byr": self._year_check(1920, 2002),
            "ecl": self._ecl_check,
            "eyr": self._year_check(2020, 2030),
            "hcl": self._pattern_match(r"^#[a-fA-F0-9]{6}$"),
            "hgt": self._hgt_check,
            "iyr": self._year_check(2010, 2020),
            "pid": self._pattern_match(r"^[0-9]{9}$"),
        }

    def parse(self, input_file):
        return [{x.split(":")[0]: x.split(":")[1] for x in p}
                for p in
                [p.split() for p in open(input_file).read().split("\n\n")]]

    def part_one(self):
        return len([x for x in self.input if self.all_req_fields(x)])

    def part_two(self):
        return len([x for x in self.input if self.validate_passport(x)])

    def all_req_fields(self, p):
        return all(x in p for x in self.validation.keys())

    def _ecl_check(self, x):
        return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def _hgt_check(self, x):
        return (
            ("cm" in x and 150 <= int(x.replace("cm", "")) <= 193) or
            ("in" in x and 59 <= int(x.replace("in", "")) <= 76)
        )

    def _pattern_match(self, pattern):
        def matched(x):
            return bool(re.match(pattern, x))
        return matched

    def _year_check(self, lower, upper):
        def check(x):
            return lower <= int(x) <= upper
        return check

    def validate_field(self, key, val):
        return key in self.validation.keys() and self.validation[key](val)

    def validate_passport(self, p):
        return (self.all_req_fields(p) and
                all([self.validate_field(k, v)
                     for k, v in p.items() if k != 'cid']))

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s != None:  # Noqa E203
            print(f"Part Two: {s}")
