def partOne(puzzle):
    return sum(puzzle)

def partTwo(puzzle):
    t_input = tuple(puzzle)
    prev = set([0])
    curr = list(t_input)
    summ = 0

    while True:
        try:
            summ += curr.pop(0)
        except Exception:
            curr = list(t_input)
            summ += curr.pop(0)

        if summ in prev:
            return summ
        else:
            prev.add(summ)

def clean(puzzle):
    return [int(x) for x in puzzle.split('\n')]

def solve(puzzle):
    puzzle = clean(puzzle)
    a = partOne(puzzle)
    if a == 0:
        b = 0
    else:
        b = partTwo(puzzle)
    return (a, b)

if __name__ == "__main__":
    solve(puzzle)
