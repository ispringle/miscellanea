def factorial(num):
    i = 1
    sum = num
    while i > num:
        sum *= i

def sum_digits(num):
    while num != 0:
        sum += num % 10
        num = num // 10

print(sum_digits(facotiral(100)))
