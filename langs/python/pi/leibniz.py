def calc_pi(n):
    numerator = 4.0
    denominator = 1.0
    operator = 1.0
    pi = 0.0
    for _ in range(n):
        pi += operator * (numerator / denominator)
        denominator += 2.0
        operator *= -1.0
    return pi


if __name__ == "__main__":
    print(calc_pi(1000000))
