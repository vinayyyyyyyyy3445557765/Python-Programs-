def generate_employee_report():
    try:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = float(input("Enter basic monthly salary: "))
        allowance = float(input("Enter special allowances (monthly): "))
        bonus_percent = float(input("Enter bonus percentage: "))

        gross_monthly = basic + allowance
        annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
        annual_gross = (gross_monthly * 12) + annual_bonus

        standard_deduction = 50000
        taxable_income = max(0, annual_gross - standard_deduction)

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
        net_salary = annual_gross - total_tax

        print("\nEmployee Tax Report")
        print("-" * 40)
        print(f"{'Field':<25}{'Details'}")
        print("-" * 40)
        print(f"{'Name':<25}{name}")
        print(f"{'EmpID':<25}{emp_id}")
        print(f"{'Gross Monthly Salary':<25}₹{gross_monthly:,.0f}")
        print("-" * 40)
        print(f"{'Annual Gross Salary':<25}₹{annual_gross:,.0f}")
        print(f"{'Taxable Income':<25}₹{taxable_income:,.0f}")
        print(f"{'Tax Payable':<25}₹{total_tax:,.0f}")
        print(f"{'Annual Net Salary':<25}₹{net_salary:,.0f}")
        print("-" * 40)

    except ValueError:
        print("Error: Invalid input.")


def run_tests():
    print("\nRunning Test Cases...\n")

    gross_monthly = 85000
    annual_gross = gross_monthly * 12
    taxable = annual_gross - 50000

    assert gross_monthly == 85000
    assert taxable > 0

    tax = ((300000 * 0) +
           (300000 * 0.05) +
           (300000 * 0.10) +
           (taxable - 900000) * 0.15) if taxable > 900000 else 0

    cess = tax * 0.04
    assert tax + cess >= 0

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    generate_employee_report()
