def reverse_number():
    num = int(input("Enter a number: "))
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reverse:", reverse)

if __name__ == "__main__":
    reverse_number()
