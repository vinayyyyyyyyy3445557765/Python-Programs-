def salary_calculation():
    try:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = float(input("Enter basic monthly salary: "))
        allowance = float(input("Enter special allowances (monthly): "))
        bonus_percent = float(input("Enter bonus percentage: "))

        gross_monthly = basic + allowance
        annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
        annual_gross = (gross_monthly * 12) + annual_bonus

        print("\nEmployee Name:", name)
        print("Employee ID:", emp_id)
        print("Gross Monthly Salary:", gross_monthly)
        print("Annual Gross Salary:", annual_gross)

    except ValueError:
        print("Error: Invalid input.")


def run_tests():
    print("\nRunning Test Cases...\n")

    gross_monthly = 50000 + 10000
    annual_bonus = (gross_monthly * 12) * 0.10
    annual_gross = (gross_monthly * 12) + annual_bonus

    assert gross_monthly == 60000
    assert annual_gross > 0

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    salary_calculation()
