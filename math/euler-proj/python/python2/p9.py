#Find the only Pythagorean triplet where a + b + c = 1000

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c_sq = a**2 + b**2
        c = c_sq**.5

        if a + b + c == 1000:
            print a, b, c
            print a * b * c
            break