from itertools import zip_longest as zip
c = [int(x.strip()) for z in open('input.txt')
     for y in z.split(' -> ') for x in y.split(',')]
m1 = [0] * (
    (1 + (xm := max([c[i] for i in range(0, len(c), 2)]))) *
    (1 + (ym := max([c[i] for i in range(1, len(c), 2)]))))
for i in range(0, len(c), 4):
    if (dx := abs((x1 := c[i]) - (
         x2 := c[i+2]))) != (dy := abs((y1 := c[i+1]) - (y2 := c[i+3]))):
        for ix, iy in zip(range(0, dx + 1 if dx else 0),
                          range(0, dy + 1 if dy else 0), fillvalue=0):
            m1[(min(x1, x2) + ix) + (min(y1, y2) + iy) * xm] += 1
m2 = [0] * ((1 + xm) * (1 + ym))
for i in range(0, len(c), 4):
    dx, dy = map(lambda x: 1 if x > 0 else 0 if x == 0 else -1,
                 ((x2 := c[i+2]) - (x1 := c[i]),
                  (y2 := c[i+3]) - (y1 := c[i+1])))
    m2[x1 + y1 * xm] += 1
    while x1 != x2 or y1 != y2:
        x1, y1 = x1 + dx, y1 + dy
        m2[x1 + y1 * xm] += 1
print(f"Part 1: {(s := lambda a: sum([1 for x in a if x > 1]))(m1)}\
        Part 2: {s(m2)}")
