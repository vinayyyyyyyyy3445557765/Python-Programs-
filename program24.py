def display_series():
    n = int(input("Enter N: "))
    print()
    a, b = 1, 1

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print("\n")


def run_tests():
    series = []
    a, b = 1, 1
    while a <= 21:
        series.append(a)
        a, b = b, a + b

    assert series == [1, 1, 2, 3, 5, 8, 13, 21]
    print("Test passed\n")


if __name__ == "__main__":
    run_tests()
    display_series()
