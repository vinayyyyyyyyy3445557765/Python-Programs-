def calculate_loyalty_points(grand_total):
    points = grand_total // 100
    return points

def display_invoice(grand_total):
    print(f"Grand Total: ₹{grand_total}")
    points = calculate_loyalty_points(grand_total)
    print(f"Loyalty Points Earned: {points}\n")

def run_loyalty_program():
    try:
        grand_total = float(input("Enter the final grand total (₹): "))
        display_invoice(grand_total)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    run_loyalty_program()
