# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857

from lib.prime_factor import prime_factors

number = 600851475143 

factors = prime_factors(number)
print(max(factors))
