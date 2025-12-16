def find_largest():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))

        return max(a, b, c)
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None


def run_tests():
    print("\nRunning Test Cases...\n")

    assert max(10, 20, 30) == 30
    assert max(-10, -5, -20) == -5
    assert max(5, 5, 5) == 5
    assert max(1.5, 2.5, 0.5) == 2.5

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()

    result = find_largest()
    if result is not None:
        print("\nLargest number is:", result)
