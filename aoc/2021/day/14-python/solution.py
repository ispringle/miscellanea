from collections import Counter


def naive(polymer, rules, steps=10):
    def expand(polymer, rules, new_polymer=""):
        for i in range(len(polymer) - 1):
            new_polymer += (f := polymer[i]) + rules[f + polymer[i + 1]]
        return new_polymer + polymer[-1]

    for _ in range(steps):
        polymer = expand(polymer, rules)
    return max(c := Counter(polymer).values()) - min(c)


def count_pairs(polymer, rules, steps=40):
    pairs = Counter(map(str.__add__, polymer, polymer[1:]))
    elements = Counter(polymer)
    for _ in range(steps):
        for molecule, count in pairs.copy().items():
            pairs[molecule] -= count
            pairs[molecule[0] + (e := rules[molecule])] += count
            pairs[e + molecule[-1]] += count
            elements[e] += count
    return max(ev := elements.values()) - min(ev)


def main(input):
    polymer, rules = (i := [*open(input)])[0].strip(), {
        (y := x.split(" -> "))[0]: y[1].strip() for x in i[2:]}
    print(naive(polymer, rules))
    print(count_pairs(polymer, rules))


if __name__ == "__main__":
    main("input.txt")
