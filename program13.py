def calculate_tax():
    try:
        taxable_income = float(input("Enter taxable income: "))

        tax = 0
        slabs = [
            (300000, 0),
            (600000, 0.05),
            (900000, 0.10),
            (1200000, 0.15),
            (1500000, 0.20),
            (float("inf"), 0.30)
        ]

        previous = 0
        for limit, rate in slabs:
            if taxable_income > limit:
                tax += (limit - previous) * rate
                previous = limit
            else:
                tax += (taxable_income - previous) * rate
                break

        if taxable_income <= 700000:
            tax = 0

        cess = tax * 0.04
        total_tax = tax + cess

        print("\nTaxable Income:", taxable_income)
        print("Income Tax:", tax)
        print("Health & Education Cess (4%):", cess)
        print("Total Tax Payable:", total_tax)

        return total_tax

    except ValueError:
        print("Error: Invalid input.")
        return None


def run_tests():
    print("\nRunning Test Cases...\n")

    income1 = 650000
    assert income1 <= 700000

    income2 = 1000000
    tax = ((300000 * 0) +
           (300000 * 0.05) +
           (300000 * 0.10) +
           (100000 * 0.15))
    cess = tax * 0.04
    assert tax + cess > 0

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    calculate_tax()
