def display_series():
    n = int(input("Enter N: "))
    current = 1
    diff = 1

    print()
    while current <= n:
        print(current, end=" ")
        current += diff
        diff += 1
    print("\n")


def run_tests():
    series = []
    current = 1
    diff = 1

    while current <= 22:
        series.append(current)
        current += diff
        diff += 1

    assert series == [1, 2, 4, 7, 11, 16, 22]
    print("Test passed\n")


if __name__ == "__main__":
    run_tests()
    display_series()
