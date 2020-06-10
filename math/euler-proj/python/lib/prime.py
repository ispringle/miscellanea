# Functions related to prime numbers

from functools import reduce


class known:
    primes = [2, 3, 5]


# Brute force primality test
def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    if n not in known.primes:
        known.primes.append(n)
    return True


def sieve(n):
    sieve = [i for i in range(3, n + 1) if i % 2 != 0]
    for p in sieve:
        if p:
            if p * p > n:
                break
            for q in range(p * p, n + 1, 2 * p):
                sieve[(q - 3) // 2] = 0
    return [2] + list(filter(None, sieve))


def get_nth_prime(n):
    if len(known.primes) >= n:
        return known.primes[n - 1]
    lastPrime = known.primes[-1]
    while len(known.primes) < n:
        is_prime(lastPrime)
        lastPrime += 2
    return known.primes[n - 1]


def primes_below(n):
    if known.primes[-1] > n:
        return [i for i in known.primes if i <= n]
    lastPrime = known.primes[-1] + 2
    while lastPrime <= n:
        is_prime(lastPrime)
        lastPrime += 2
    return [i for i in known.primes if i <= n]


def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            num /= i
            factors.append(i)
        i += 2
    if num > 1:
        factors.append(num)
    oldFactors = factors
    factors = list(set(factors))
    for i in factors:
        if oldFactors.count(i) > 1:
            factors.pop(factors.index(i))
            exp = []
            for j in range(oldFactors.count(i)):
                exp.append(i)
            factors.append(exp)
    return factors


def new_prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            num /= i
            factors.append(i)
        i += 2
    if num > 1:
        factors.append(num)
    oldFactors = factors
    factors = list(set(factors))
    for i in factors:
        if oldFactors.count(i) > 1:
            factors.pop(factors.index(i))
            exp = []
            for j in range(oldFactors.count(i)):
                exp.append(i)
            factors.append(exp)
    return factors


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def GCD(numbers):
    return reduce(lambda a, b: gcd(a, b), numbers)


def lcm(a, b):
    return a * b // gcd(a, b)


def LCM(numbers):
    result = 1
    for i in numbers:
        result = lcm(result, i)
    return result
