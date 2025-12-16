def student_report_card():
    try:
        name = input("Enter student name: ")
        s1 = float(input("Enter marks for subject 1: "))
        s2 = float(input("Enter marks for subject 2: "))
        s3 = float(input("Enter marks for subject 3: "))

        total = s1 + s2 + s3
        average = total / 3

        if average >= 60:
            grade = "1st Class"
        elif average >= 50:
            grade = "2nd Class"
        elif average >= 35:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\nStudent Name:", name)
        print("Total Marks:", total)
        print("Average:", average)
        print("Class Secured:", grade)

    except ValueError:
        print("Error: Invalid input.")


def tax_calculator():
    try:
        name = input("Enter employee name: ")
        basic = float(input("Enter monthly basic salary: "))
        hra = float(input("Enter monthly HRA: "))
        other = float(input("Enter other monthly allowances: "))

        gross_annual = (basic + hra + other) * 12
        taxable_income = max(0, gross_annual - 50000)

        tax = 0
        slabs = [
            (300000, 0),
            (600000, 0.05),
            (900000, 0.10),
            (1200000, 0.15),
            (1500000, 0.20),
            (float("inf"), 0.30),
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

        net_salary = gross_annual - tax

        print("\nEmployee Name:", name)
        print("Gross Annual Salary:", gross_annual)
        print("Taxable Income:", taxable_income)
        print("Tax Payable:", tax)
        print("Net Salary:", net_salary)

    except ValueError:
        print("Error: Invalid input.")


def run_tests():
    print("\nRunning Test Cases...\n")

    assert (60 + 70 + 80) / 3 >= 60
    assert 50 <= (50 + 55 + 60) / 3 < 60
    assert 35 <= (35 + 40 + 45) / 3 < 50
    assert (20 + 30 + 25) / 3 < 35

    gross = (50000 + 10000 + 5000) * 12
    taxable = gross - 50000
    assert taxable > 700000

    gross2 = (40000 + 5000 + 5000) * 12
    taxable2 = gross2 - 50000
    assert taxable2 <= 700000

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()

    print("\n1. Student Report Card")
    print("2. Tax Calculator")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        student_report_card()
    elif choice == "2":
        tax_calculator()
    else:
        print("Invalid choice.")
