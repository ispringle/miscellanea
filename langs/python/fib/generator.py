def fib(n):
    yield 0
    if n > 0:
        yield 1
    prev = 0
    curr = 1
    for _ in range(n-1):
        prev, curr = curr, prev + curr
        yield curr


if __name__ == "__main__":
    for i in fib(10):
        print(i)
