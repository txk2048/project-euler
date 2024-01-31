def main():
    total = 0
    a = 1
    b = 2

    while b <= 4_000_000:
        if b % 2 == 0:
            total += b

        a, b = b, a + b

    print(total)


if __name__ == "__main__":
    main()
