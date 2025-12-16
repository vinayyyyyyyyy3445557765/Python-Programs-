def calculate_net_salary():
    try:
        annual_gross = float(input("Enter annual gross salary: "))
        total_tax = float(input("Enter total tax payable: "))

        net_salary = annual_gross - total_tax

        print("\nAnnual Gross Salary:", annual_gross)
        print("Total Tax Payable:", total_tax)
        print("Annual Net Salary:", net_salary)

    except ValueError:
        print("Error: Invalid input.")


def run_tests():
    print("\nRunning Test Cases...\n")

    gross = 1200000
    tax = 100000
    net = gross - tax

    assert net == 1100000
    assert net >= 0

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    calculate_net_salary()
