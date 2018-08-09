# Summation of prime
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# Answer: 142913828922

from lib.prime import *

goal = 2000000

print(sum(sieve(goal)))

