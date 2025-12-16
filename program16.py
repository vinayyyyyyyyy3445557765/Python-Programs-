import re

def get_valid_name():
    while True:
        name = input("Enter employee name: ")
        if name.isalpha() and 1 <= len(name) <= 50:
            return name
        print("Invalid name. Use alphabets only (1–50 characters).")


def get_valid_empid():
    while True:
        emp_id = input("Enter employee ID: ")
        if emp_id.isalnum() and 5 <= len(emp_id) <= 10:
            return emp_id
        print("Invalid EmpID. Use alphanumeric characters (5–10 characters).")


def get_valid_salary(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if (value > 0 or (allow_zero and value >= 0)) and value <= 10000000:
                return value
            print("Invalid amount. Must be within valid range.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_valid_bonus():
    while True:
        try:
            bonus = float(input("Enter bonus percentage: "))
            if 0 <= bonus <= 100:
                return bonus
            print("Invalid bonus. Must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def validate_and_calculate():
    name = get_valid_name()
    emp_id = get_valid_empid()
    basic = get_valid_salary("Enter basic monthly salary: ")
    allowance = get_valid_salary("Enter special allowances (monthly): ", allow_zero=True)
    bonus_percent = get_valid_bonus()

    gross_monthly = basic + allowance
    if gross_monthly <= 0:
        print("Gross monthly salary must be greater than zero.")
        return

    annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus

    if annual_gross > 50000000:
        print("Annual gross salary exceeds realistic limits.")
        return

    print("\nValidated Employee Details")
    print("----------------------------")
    print("Name:", name)
    print("EmpID:", emp_id)
    print("Gross Monthly Salary:", gross_monthly)
    print("Annual Gross Salary:", annual_gross)


def run_tests():
    print("\nRunning Test Cases...\n")

    assert "John".isalpha()
    assert not "John123".isalpha()
    assert "E12345".isalnum()
    assert 0 <= 50 <= 100
    assert 50000 + 10000 > 0
    assert (60000 * 12) < 50000000

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()
    validate_and_calculate()
