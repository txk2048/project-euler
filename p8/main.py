import os
import collections
import itertools
import math


def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


def main():
    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        digits = ""
        for line in f:
            digits += line.strip()

    max_product = 0
    for window in sliding_window(digits, 13):
        product = math.prod(map(int, window))
        max_product = max(max_product, product)

    print(max_product)


if __name__ == "__main__":
    main()
