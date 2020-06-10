# Longest Collatz Sequence
# Answer: 837799

from lib.math import collatz

upper = 1000000
max = {"n": 0, "len": 0}


def countCC(max, n):
    chain = collatz(n)
    if len(chain) > max["len"]:
        max["len"] = len(chain)
        max["n"] = n


for i in range(1, upper - 1):
    countCC(max, i)
print(max)
