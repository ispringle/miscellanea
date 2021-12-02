def clean_input(unclean_input):
    return [int(x) for x in unclean_input.split("\n")]


def calc_fuel(mass):
    return int((mass / 3) - 2)


def calc_fuel_for_fuel(total_mass, fuel_mass):
    if fuel_mass > 0:
        return calc_fuel_for_fuel(total_mass + fuel_mass, calc_fuel(fuel_mass))
    return total_mass


def solve_a(masses):
    return sum([calc_fuel(x) for x in masses])


def solve_b(masses):
    return sum([calc_fuel_for_fuel(x, calc_fuel(x)) for x in
               [calc_fuel(y) for y in masses]])


def solve(puzzle):
    masses = clean_input(puzzle)
    a = solve_a(masses)
    b = solve_b(masses)
    return (a, b)


if __name__ == "__main__":
    import sys
    print(solve(sys.argv[1]))

