def calculate_grand_total():
    n = int(input("Enter number of items: "))
    grand_total = 0

    print()
    for _ in range(n):
        code = input("Enter item code: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        item_total = qty * price

        if code.upper() == "PROMO10":
            discount = item_total * 0.10
            item_total -= discount
            print("Promotional Discount Applied:", discount)

        grand_total += item_total
        print("Item Total:", item_total)
        print()

    print("Final Grand Total:", grand_total)


if __name__ == "__main__":
    calculate_grand_total()
