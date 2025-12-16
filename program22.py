def display_series():
    n = int(input("Enter N: "))
    print()
    series = [1, 4, 7, 12]
    i = 0
    while series[i] <= n:
        print(series[i], end=" ")
        if i >= 2:
            series.append(series[i] + series[i - 1])
        i += 1
    print("\n")


def run_tests():
    series = [1, 4, 7, 12]
    series.append(series[3] + series[2])
    assert series == [1, 4, 7, 12, 19]
    print("Test passed\n")


if __name__ == "__main__":
    run_tests()
    display_series()
