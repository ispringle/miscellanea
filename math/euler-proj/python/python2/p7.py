#Euler Project #7 - What is the 10 001st prime number?

primes = []
i = 2

def is_prime(n):
    if n == 2:
        primes.append(n)
        return
    if n == 3:
        primes.append(n)
        return
    if n % 2 == 0:
        return
    if n % 3 == 0:
        return

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return
        i += w
        w = 6 - w
    primes.append(n)
    return

def next_prime(n):
    global i
    n = i
    is_prime(n)
    i += 1

while len(primes) < 10001:
    next_prime(i)
print max(primes)
