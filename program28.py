def calculate_final_amount():
    grand_total = float(input("Enter grand total after discounts: "))
    member = input("Is customer a member (y/n): ").lower()

    if member == 'y':
        discount = grand_total * 0.02
        grand_total -= discount
        print("Membership Discount Applied:", discount)
    else:
        print("No Membership Discount Applied")

    print("Final Payable Amount:", grand_total)


if __name__ == "__main__":
    calculate_final_amount()
