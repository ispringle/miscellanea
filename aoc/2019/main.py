import sys
import timeit
from importlib import import_module

from aocd.models import Puzzle
from aocd import submit as _submit


def submit(solutions, year, day):
    day = int(day)
    year = int(year)

    if solutions[0] and not solutions[1]:
        _submit(solutions[0], part="a", day=day, year=year)
    elif solutions[1]:
        _submit(solutions[0], part="a", day=day, year=year)
        _submit(solutions[1], part="b", day=day, year=year)
    else:
        print("Something might be wrong with the returned solution!")

if __name__ == "__main__":
    year = int(sys.argv[1])
    day  = int(sys.argv[2])

    puzzle = Puzzle(year=year, day=day)

    day = str(day)
    if len(day) == 1:
        day = "0" + day

    try:
        solver = import_module(f"{year}.{day}.Solution")
    except ModuleNotFoundError:
        print("No module has been created for AOC {year}/{day} yet!")
    start = timeit.default_timer()
    solutions = solver.solve(puzzle.input_data)
    total_time = timeit.default_timer() - start

    submit(solutions, year, day)

    if solutions[0]:
        print(f"You answer to AOC-{year} day {day}, part one is:")
        print(solutions[0])
    if solutions[1]:
        print(f"You answer to AOC-{year} day {day}, part two is:")
        print(solutions[1])
    print(f"Solution was found in {total_time}ms")

