def swap_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        a, b = b, a
        return a, b

    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None


def run_tests():
    print("\nRunning Test Cases...\n")

    x, y = 10, 20
    x, y = y, x
    assert (x, y) == (20, 10)

    x, y = -5, 5
    x, y = y, x
    assert (x, y) == (5, -5)

    x, y = 0, 0
    x, y = y, x
    assert (x, y) == (0, 0)

    x, y = 1.5, 2.5
    x, y = y, x
    assert (x, y) == (2.5, 1.5)

    print(" All test cases passed successfully!")


if __name__ == "__main__":
    run_tests()

    a, b = swap_numbers()
    if a is not None:
        print(f"\nAfter Swapping:")
        print(f"First number: {a}")
        print(f"Second number: {b}")
