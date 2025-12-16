def display_series():
    n = int(input("Enter N: "))
    print()

    current = 1
    diffs = [4, 4, 4, 8, 4, 4, 8, 4]
    i = 0

    while current <= n:
        print(current, end=" ")
        if i < len(diffs):
            current += diffs[i]
            i += 1
        else:
            break

    print("\n")


def run_tests():
    series = []
    current = 1
    diffs = [4, 4, 4, 8, 4, 4, 8, 4]

    for d in diffs:
        series.append(current)
        current += d
    series.append(current)

    assert series == [1, 5, 9, 13, 21, 25, 29, 37, 41]
    print("Test passed\n")


if __name__ == "__main__":
    run_tests()
    display_series()
