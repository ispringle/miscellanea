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

    solutions = solver.solve()
    if solutions[1] and not solutions[1]:
        submit(solutions[0], part="a", day=day, year=year)
        print(solutions[0])
    elif solutions[2]:
        submit(solutions[0], part="a", day=day, year=year)
        submit(solutions[1], part="b", day=day, year=year)
        print(solution[0])
        print(solution[1])
    else:
        print("Something might be wrong with the returned solution!")
        print(solution)
