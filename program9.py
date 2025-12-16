def check_leap_year():
    try:
        year = int(input("Enter a year: "))
        return check_year(year)
    except ValueError:
        print("Error: Please enter a valid year.")
        return None


def check_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def run_tests():
    print("\nRunning Test Cases...\n")

    assert check_year(2000) == True
    assert check_year(1900) == False
    assert check_year(2024) == True
    assert check_year(2023) == False

    print("All test cases passed successfully.")


if __name__ == "__main__":
    run_tests()

    result = check_leap_year()
    if result is not None:
        if result:
            print("\nIt is a leap year.")
        else:
            print("\nIt is not a leap year.")
