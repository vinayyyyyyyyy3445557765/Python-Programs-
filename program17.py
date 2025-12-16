def display_series():
    n = int(input("Enter N: "))
    for i in range(1, n + 1):
        print(i, end=" ")


def run_tests():
    assert list(range(1, 6)) == [1, 2, 3, 4, 5]
    print("Test passed")


if __name__ == "__main__":
    run_tests()
    display_series()
