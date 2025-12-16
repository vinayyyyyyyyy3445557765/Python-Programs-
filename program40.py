def print_factorial_pattern():
    n = int(input("Enter number of rows: "))
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        print(fact, end=" ")

    print()

if __name__ == "__main__":
    print_factorial_pattern()
