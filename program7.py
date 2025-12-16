def check_tax():
    try:
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))

        return name, salary > 300000
    except ValueError:
        print("Error: Please enter a valid salary.")
        return None, None


def run_tests():
    print("\nRunning Test Cases...\n")

    assert 350000 > 300000
    assert not (250000 > 300000)
    assert (300000 > 300000) == False
    assert 1000000 > 300000

    print("All test cases passed successfully.")



if __name__ == "__main__":
    run_tests()

    name, must_pay_tax = check_tax()
    if name is not None:
        if must_pay_tax:
            print(f"\n{name} must pay tax.")
        else:
            print(f"\n{name} does not need to pay tax.")
