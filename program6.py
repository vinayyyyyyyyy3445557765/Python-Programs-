def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        return "Even" if number % 2 == 0 else "Odd"
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None


def run_tests():
    print("\nRunning Test Cases...\n")

    assert (10 % 2 == 0) is True
    assert (7 % 2 == 0) is False
    assert (0 % 2 == 0) is True
    assert (-4 % 2 == 0) is True
    assert (-3 % 2 == 0) is False

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()

    result = check_even_odd()
    if result is not None:
        print("\nThe number is:", result)
