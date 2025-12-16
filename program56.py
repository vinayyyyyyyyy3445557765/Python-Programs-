def sum_2d_array():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    total = 0

    for i in range(r):
        for j in range(c):
            total += int(input(f"Enter element [{i}][{j}]: "))

    print("Sum of all elements:", total)

if __name__ == "__main__":
    sum_2d_array()
