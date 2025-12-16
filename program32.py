def check_minimum_purchase(grand_total):
    if grand_total < 500:
        print("Minimum purchase amount of ₹500 not met. Cannot generate invoice.\n")
    else:
        print(f"Invoice can be generated. Grand Total: ₹{grand_total}\n")

def run_minimum_purchase_check():
    try:
        grand_total = float(input("Enter the final grand total (₹): "))
        check_minimum_purchase(grand_total)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    run_minimum_purchase_check()
