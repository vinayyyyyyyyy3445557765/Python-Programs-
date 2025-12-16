def apply_payment_surcharge(grand_total, payment_mode):
    if payment_mode.lower() == 'credit card':
        surcharge = grand_total * 0.02
    else:
        surcharge = 0
    return surcharge

def generate_invoice_payment_mode(grand_total, payment_mode):
    surcharge = apply_payment_surcharge(grand_total, payment_mode)
    final_amount = grand_total + surcharge

    print(f"Payment Method: {payment_mode}")
    print(f"Surcharge Amount: ₹{surcharge:.2f}")
    print(f"Final Payable Amount: ₹{final_amount:.2f}\n")

def run_payment_mode():
    try:
        grand_total = float(input("Enter the final grand total (₹): "))
        payment_mode = input("Enter payment method (Cash/Credit Card): ")
        generate_invoice_payment_mode(grand_total, payment_mode)
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    run_payment_mode()
