_, dots, folds = (i := open("test.txt").read().split("\n\n")), set(
    tuple(map(int, x.split(','))) for x in i[0].split()), i[-1]
first = True
for fold in folds.strip().split("\n"):
    axis, coord = (i := fold.strip("fold along ").split("="))[0], int(i[-1])
    new_dots = set()
    for loc in dots:
        x, y = loc
        if axis == 'y' and y > coord:
            new_coord = (x, (2 * coord) - y)
        elif axis == 'x' and x > coord:
            new_coord = ((2 * coord) - x, y)
        else:
            new_coord = (x, y)
        new_dots.add(new_coord)
    dots = new_dots
    print(len(dots)) if first else ()
    first = False
message = "\n".join([''.join(
    ["#" if (x, y) in dots else " " for x in range(max(n[0] for n in dots))])
    for y in range(max(n[-1] for n in dots))])
print(message)
