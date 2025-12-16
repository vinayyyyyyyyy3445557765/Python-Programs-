def separate_whole_fraction():
    num = float(input("Enter a double value: "))

    whole = int(num)
    fraction = num - whole

    print("Whole value:", whole)
    print("Fractional value:", fraction)

if __name__ == "__main__":
    separate_whole_fraction()
