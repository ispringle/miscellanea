#Euler Problem 2. Sum of all even number in the Fib. Seq. which do not exceen 4,000,000.
#Solved!

fib = [0]
fs = 0
fa = 1
fb = 1

def F(count):
    global fs
    while fs < count:
        global fa, fb
        fs = fa+fb
        if fs <= count:
            fib.append(fs)
            fb = fa
            fa = fs
        #print fib

def rm_odd(l):
    print sum(e for e in l if e % 2 == 0)

F(4000000)
rm_odd(fib)
