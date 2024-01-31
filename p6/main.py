def main():
    sum_of_squares = sum(x**2 for x in range(1, 101))
    square_of_sum = sum(range(1, 101)) ** 2

    print(square_of_sum - sum_of_squares)


if __name__ == "__main__":
    main()
