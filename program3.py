def calculate_discount():
    try:
        total_amount = float(input("Enter total amount: "))
        discount_percentage = float(input("Enter discount percentage: "))

        discount = (total_amount * discount_percentage) / 100
        final_amount = total_amount - discount

        return discount, final_amount

    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None


def run_tests():
    print("\nRunning Test Cases...\n")

    assert (1000 * 10) / 100 == 100
    assert 1000 - ((1000 * 10) / 100) == 900

    assert (500 * 0) / 100 == 0
    assert 500 - ((500 * 0) / 100) == 500

    assert (0 * 10) / 100 == 0
    assert 0 - ((0 * 10) / 100) == 0

    assert (1500 * 12.5) / 100 == 187.5
    assert 1500 - ((1500 * 12.5) / 100) == 1312.5

    print(" All test cases passed successfully!")


if __name__ == "__main__":
    run_tests()

    discount, final_amount = calculate_discount()
    if discount is not None:
        print(f"\nDiscount Amount: {discount}")
        print(f"Final Amount to Pay: {final_amount}")
