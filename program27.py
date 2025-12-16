def calculate_final_amount():
    grand_total = 0
    total_qty = 0

    n = int(input("Enter number of items: "))
    print()

    for _ in range(n):
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        item_total = qty * price
        grand_total += item_total
        total_qty += qty

        print("Item Total:", item_total)
        print()

    print("Initial Grand Total:", grand_total)

    if grand_total > 10000:
        discount = grand_total * 0.10
        grand_total -= discount
        print("10% Discount Applied:", discount)

    if total_qty > 20:
        qty_discount = grand_total * 0.05
        grand_total -= qty_discount
        print("5% Quantity Discount Applied:", qty_discount)

    print("Final Payable Amount:", grand_total)


if __name__ == "__main__":
    calculate_final_amount()
