# Functions related to mathematics and numbers (which don't fit elsewhere)

def iter_int(n):
	iterable = []
	while n:
		digit = n % 10
		n //= 10
		iterable.insert(0, digit)
	return iterable
