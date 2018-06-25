#Euler project 16, What is the sum of the digits of the number 2^1000?

s = 2**1000

def add_digit(s):
    digits = list(str(s))
    return sum([int(i) for i in digits])
print add_digit(s)
