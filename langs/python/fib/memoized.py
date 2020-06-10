def fib(n):
    def _fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    memo = {0: 0, 1: 1}
    return _fib(n)


if __name__ == "__main__":
    print(fib(10))  # 10th Fibonacci number is 55
