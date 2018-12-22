# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

def palindrome(number):
	return (str(number) == str(number)[::-1])

palindromes = []

for x in range(999):
	for y in range(999):
		if palindrome(x * y):
			palindromes.append(x * y)

print(max(palindromes))
