def print_fibonacci_series():
    n = int(input("Enter number of terms: "))

    a, b = 1, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

if __name__ == "__main__":
    print_fibonacci_series()
