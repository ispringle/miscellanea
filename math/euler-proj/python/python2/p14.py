#Euler project 14, which number, under 1000000, in collatz conjecture produces the longest chain
max_initial = 0
max_chain = 0

def collatz(n):
    global chains, max_initial, max_chain
    chain = []
    initial_n = n

    if n == 1:
        chain.append(n)
        n = 4
    while n > 1:
        chain.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
    if n == 1:
        chain.append(n)

    #result = [initial_n, len(chain)]
    #chains.append(result)

    if len(chain) > max_chain:
        max_chain = len(chain)
        max_initial = initial_n



max(((collatz(i),i) for i in range(1,1000000)))
print max_initial + "is the largest number under 1,000,000 that produces the largest chain in Collatz Conjecture."
