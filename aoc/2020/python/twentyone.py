from collections import Counter, defaultdict


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [((a := x.strip().split("(contains"))[0].split(),
                 a[1].replace(",", "").replace(")", "").split())
                for x in open(input_file).readlines()]

    def part_one(self):
        count, foods = Counter(), defaultdict(list)
        for item in self.input:
            ingredients, allergies = item
            for allergen in allergies:
                foods[allergen].append(set(ingredients))
            for ingredient in ingredients:
                count[ingredient] += 1
        self.foods = {k: set.intersection(*v) for k, v in foods.items()}
        safe = set.union(*self.foods.values())
        return sum(v for k, v in count.items() if k not in safe)

    def part_two(self):
        matching = []
        foods = self.foods
        while foods:
            allergen, ingredient = next((k, v)
                                        for k, v in foods.items()
                                        if len(v) == 1)
            matching.append((allergen, next(iter(ingredient))))
            foods = {k: v - ingredient
                     for k, v in foods.items()
                     if k != allergen}
        return ",".join(ingredient
                        for allergen, ingredient in sorted(matching))

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
