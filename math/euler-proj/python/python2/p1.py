#Euler Problem 1. Sum of all multiples of 3 and 5 between 0 and 1000, but not including 1000 or duplicates (multiples of both 3 and 5)
#Solved!

def multiples(m, x, count):

    mul = [0]

    mu = 0
    mx = 0
    while mu <= count:
        mu = mu+m
        if mu < count:
            mul.append(mu)
            print mu

    while mx <= count:
        mx = mx+x
        if mx < count:
            mul.append(mx)
            print mx
    if mx >= count:
        print set(mul)
        print sum(set(mul))

multiples(3, 5,1000)
