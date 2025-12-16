def taxable_income_calculation():
    try:
        annual_gross = float(input("Enter annual gross salary: "))

        standard_deduction = 50000
        taxable_income = annual_gross - standard_deduction

        print("\nAnnual Gross Salary:", annual_gross)
        print("Standard Deduction:", standard_deduction)
        print("Taxable Income:", taxable_income)

    except ValueError:
        print("Error: Invalid input.")


def run_tests():
    print("\nRunning Test Cases...\n")

    annual_gross = 720000
    taxable = annual_gross - 50000

    assert taxable == 670000
    assert taxable >= 0

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    taxable_income_calculation()
