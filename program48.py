def maximum_in_array():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    maximum = arr[0]
    for val in arr:
        if val > maximum:
            maximum = val

    print("Maximum:", maximum)

if __name__ == "__main__":
    maximum_in_array()
