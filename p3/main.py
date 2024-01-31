import math


def sieve(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    primes = []
    for i in range(len(arr)):
        if arr[i]:
            primes.append(i)

    return primes


def main():
    target = 600851475143
    primes = sieve(math.isqrt(target))
    factors = filter(lambda x: target % x == 0, primes)

    result = max(factors)
    print(result)


if __name__ == "__main__":
    main()
