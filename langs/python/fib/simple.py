def fib(n):
    if n == 0:
        return n
    prev = 0
    curr = 1
    for _ in range(n-1):
        nxt = prev + curr
        prev = curr
        curr = nxt
    return curr


if __name__ == "__main__":
    print(fib(10))  # 10th Fibonacci number is 55
