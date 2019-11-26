import sys
from importlib import import_module
from aocd.models import Puzzle
from aocd import submit

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

    solution = solver.solve()
    submit(solution, day=day, year=year)
