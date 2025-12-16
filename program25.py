def calculate_item_total():
    code = input("Enter item code: ")
    desc = input("Enter item description: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    total = qty * price

    print("\nItem Code:", code)
    print("Description:", desc)
    print("Item Total:", total)


if __name__ == "__main__":
    calculate_item_total()
