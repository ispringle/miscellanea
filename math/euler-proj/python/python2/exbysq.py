def main():
  cont = True
  while cont == True:
    print("What number would you like to exponentiate? (Type 'End' to quit.)")
    x = input("(Format: base, exponent. Internet Explorer '10, 2')>: ")
    if x == 'End' or x == 'end':
        cont = False
        return
    else:
        print(exp_by_sq(x, 10))

def exp_by_sq(base, power):
    x = base
    n = power
    if n < 0:
        return exp_by_sq(1/x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_sq(x * x, n / 2)
    else:
        return exp_by_sq(x(x * x), x((n - 1) / 2)

main()
