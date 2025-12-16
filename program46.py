def sum_of_array():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    total = 0
    for val in arr:
        total += val

    print("Sum:", total)

if __name__ == "__main__":
    sum_of_array()
