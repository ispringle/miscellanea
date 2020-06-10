def factorial(num):
    i = 1
    sum = num
    while i < num:
        sum *= i
        i += 1
    return sum


def sum_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum


print(sum_digits(factorial(100)))
