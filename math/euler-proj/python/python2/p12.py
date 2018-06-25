#Euler Project 12, What is the value of the first triangle number to have over five hundred divisors?

maxdiv = 0
n = 1

def calc_Tri(n):
    tn = ((n * (n + 1)) / 2)
    return tn

def divisors(tn):
    for i in xrange(1, tn+1):
        if tn % i == 0:
            divs.append(i)

def compare(x):
    global maxdiv
    if x > maxdiv:
        maxdiv = x

def factors(n):
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)


# while maxdiv < 500:
#     divisors(calc_Tri(n))
#     print divs
#     compare()
#     print maxdiv
#     n += 1

while maxdiv < 500:
    tri = calc_Tri(n)
    divs = len(factors(tri))
    compare(divs)
    #compare(len(factors(calc_Tri(n))))
    if maxdiv < 500:
        n += 1
    else:
        print max(factors(calc_Tri(n)))
# print n
# print maxdiv
# print factors(calc_Tri(n))
