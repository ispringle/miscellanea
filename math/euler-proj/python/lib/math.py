# Functions related to mathematics and numbers (which don't fit elsewhere)


def iter_int(n):
    iterable = []
    while n:
        digit = n % 10
        n //= 10
        iterable.insert(0, digit)
    return iterable


def collatz(n):
    chain = []
    if n == 1:
        chain.append(n)
        n = 4
    while n > 1:
        chain.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        if n == 1:
            chain.append(n)
    return chain


def divisors(n):
    divs = []
    divisor = 0
    while n > 1:
        divisor += 1
        if n % divisor == 0:
            divs.append(divisor)
    return divs
