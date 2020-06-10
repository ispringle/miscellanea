from lib.math import divisors

sums = {}
upper = 10000

for n in range(1, upper + 1):
    n_sum = sum(divisors(n))
    try:
        sums[n_sum].append[n]
    except:
        sums[n_sum] = [n]

tally = 0
for key in sums:
    if len(sums[key]) > 1:
        for i in sums[key]:
            tally += i

print(tally)
