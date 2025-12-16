def display_series():
    n = int(input("Enter N: "))
    print()
    i = 1
    while i * i <= n:
        print(i * i, end=" ")
        i += 1
    print("\n")


def run_tests():
    result = []
    i = 1
    while i * i <= 81:
        result.append(i * i)
        i += 1
    assert result == [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print("Test passed\n")


if __name__ == "__main__":
    run_tests()
    display_series()
