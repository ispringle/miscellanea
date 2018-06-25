#Euler Problem  #6 - Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_sq(num):
    sum = 0
    while num > 0:
        sum += (num * num)
        num -= 1
    return sum

def sq_sum(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum * sum

def diff(num):
    return sq_sum(num) -  sum_sq(num)

#print diff(100)
