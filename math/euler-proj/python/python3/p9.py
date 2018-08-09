# Special Pythagorean Triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#							 a^2 + b^2 = c^2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer: 200, 375, 425
import timeit

goalSum = 1000

# Brute Force
def triplet_brute_force(sum):
	start = timeit.default_timer()
	for a in range(3, (sum-3) // 3):
		for b in range(a + 1, (sum - 1 - a) // 2):
			c = sum - a - b
			if c**2 == a**2 + b**2:
				stop = timeit.default_timer()
				print(stop-start)
				return a, b, c

# Slightly more elegant brite force
# Find triplets whose sum is a divisor of goalSum then multiple that triplet's sides by quotient
def triplet_elegant_brute(sum):
	start = timeit.default_timer()
	for i in range(1, sum // 2):
		if sum % i == 0:
			quotient = sum // i
			for a in range(3, (i-3) // 3):
				for b in range(a + 1, (i - 1 - a) // 2):
					c = i - a - b
					if c**2 == a**2 + b**2:
						a *= quotient
						b *= quotient
						c *= quotient
						stop = timeit.default_timer()
						print(stop-start)
						return a, b, c

# Using math
def get_triplet(sum):
	start = timeit.default_timer()
	for n in range(1, sum):
		for m in range(n + 1, sum):
			if ((2* m * n) + (2 * m**2)) == sum:
				a = 2 * m * n
				b = m**2 - n**2
				c = m**2 + n**2
				stop = timeit.default_timer()
				print(stop-start)
				return a, b, c

#Find a between 1 and 499 such that b is an integer
def get_trip(sum):
	start = timeit.default_timer()
	for a in range(1, sum // 2):
		b = sum * (sum / 2 - a) / (sum - a)
		if b.is_integer():
			stop = timeit.default_timer()
			print(stop-start)
			return a, b, sum - a - b

print(triplet_brute_force(goalSum))
print(triplet_elegant_brute(goalSum))
print(get_triplet(goalSum))
print(get_trip(goalSum))
