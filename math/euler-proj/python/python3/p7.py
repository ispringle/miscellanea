# 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Answer: 104743

from lib.prime import get_nth_prime

n = 10001

print(get_nth_prime(n))
