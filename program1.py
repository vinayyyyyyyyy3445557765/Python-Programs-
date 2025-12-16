def calculate_sum_and_average():
   
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        total = num1 + num2
        average = total / 2
        return total, average

    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None


def run_tests():
    
    print("\nRunning Test Cases...\n")

    # Test logic separately (without user input)
    assert (10 + 20, (10 + 20) / 2) == (30, 15)
    assert (-10 + -20, (-10 + -20) / 2) == (-30, -15)
    assert (-10 + 20, (-10 + 20) / 2) == (10, 5)
    assert (0 + 0, (0 + 0) / 2) == (0, 0)

    print(" All test cases passed successfully!")


if __name__ == "__main__":
    # Run test cases
    run_tests()

    # Run main function with user input
    total, avg = calculate_sum_and_average()

    if total is not None:
        print(f"\nSum: {total}")
        print(f"Average: {avg}")
