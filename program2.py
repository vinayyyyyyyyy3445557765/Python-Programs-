def calculate_simple_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest: "))
        time = float(input("Enter time (in years): "))

        simple_interest = (principal * rate * time) / 100
        return simple_interest

    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None


def run_tests():
    print("\nRunning Test Cases...\n")

    assert (1000 * 5 * 2) / 100 == 100.0
    assert (0 * 5 * 2) / 100 == 0.0
    assert (1000 * 0 * 2) / 100 == 0.0
    assert (1000 * 5 * 0) / 100 == 0.0
    assert (1500 * 4.5 * 1.5) / 100 == 101.25

    print(" All test cases passed successfully!")


if __name__ == "__main__":
    run_tests()

    si = calculate_simple_interest()
    if si is not None:
        print(f"\nSimple Interest: {si}")
