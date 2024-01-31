import itertools
import operator


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def main():
    products = map(
        lambda x: operator.mul(*x), itertools.product(range(100, 1000), repeat=2)
    )
    result = max(filter(is_palindrome, products))

    print(result)


if __name__ == "__main__":
    main()
