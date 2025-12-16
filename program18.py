def display_series():
    n = int(input("Enter N: "))
    for i in range(1, n + 1, 2):
        print(i, end=" ")


def run_tests():
    assert list(range(1, 10, 2)) == [1, 3, 5, 7, 9]
    print("Test passed")


if __name__ == "__main__":
    run_tests()
    display_series()
