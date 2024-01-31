import itertools


def nth(iterable, n, default=None):
    "Returns the nth item or a default value."
    return next(itertools.islice(iterable, n, None), default)


def inc_sieve():
    factors = []

    i = 2
    while True:
        if all(i % x != 0 for x in factors):
            factors.append(i)
            yield i
        i += 1


def main():
    print(nth(inc_sieve(), 10000))


if __name__ == "__main__":
    main()
