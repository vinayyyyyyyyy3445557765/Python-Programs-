def calculate_grand_total():
    grand_total = 0

    n = int(input("Enter number of items: "))
    print()

    for _ in range(n):
        code = input("Enter item code: ")
        desc = input("Enter item description: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        item_total = qty * price
        grand_total += item_total

        print("Item Total:", item_total)
        print()

    print("Grand Total:", grand_total)


if __name__ == "__main__":
    calculate_grand_total()
