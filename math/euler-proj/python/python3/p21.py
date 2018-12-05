def d(n):
    divs = []
    if n == 1: return [0]
    x = int(n**.5)
    if x**2 == n:
       divs.append(x)
       x -= 1
    else:
        divs.append(1)
    if n % 2 != 0:
        i = 3
        s = 2
    else:
        i = 2
        s = 1
    while i <= x:
        if n % i == 0:
            divs.append(i)
            divs.append(int(n/i))
        i += s
    return divs

sums = 0
for n in range(1,10001):
    x = sum(d(n))
    if x > n:
        if sum(d(x)) == n:
            sums += n + x
print(sums)
