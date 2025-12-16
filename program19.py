def display_series():
    n = int(input("Enter N: "))
    i = 2
    while i * i <= n:
        print(i * i, end=" ")
        i += 2


def run_tests():
    result = []
    i = 2
    while i * i <= 64:
        result.append(i * i)
        i += 2
    assert result == [4, 16, 36, 64]
    print("Test passed")


if __name__ == "__main__":
    run_tests()
    display_series()
