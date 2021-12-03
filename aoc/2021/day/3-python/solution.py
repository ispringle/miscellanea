i = [list(map(int, x.strip())) for x in open('test.txt').readlines()]
print((ba_d := lambda x: int(''.join(str(y) for y in x), 2))(gb := [
    int(x >= len(i)-x) for x in list(map(sum, list(map(list, zip(*i)))))]
    ) * ba_d([int(not x) for x in gb]))
