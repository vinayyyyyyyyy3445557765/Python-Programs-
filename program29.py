def calculate_tax():
    grand_total = float(input("Enter grand total before tax: "))

    if grand_total < 5000:
        tax = grand_total * 0.05
    elif grand_total <= 20000:
        tax = grand_total * 0.10
    else:
        tax = grand_total * 0.15

    final_amount = grand_total + tax

    print("Tax Amount:", tax)
    print("Final Amount Payable:", final_amount)


if __name__ == "__main__":
    calculate_tax()
