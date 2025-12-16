def print_alternating_square_pattern():
    n = int(input("Enter number of rows: "))
    sign = 1

    for i in range(1, n + 1):
        print(sign * (i * i), end=" ")
        sign *= -1

    print()

if __name__ == "__main__":
    print_alternating_square_pattern()
