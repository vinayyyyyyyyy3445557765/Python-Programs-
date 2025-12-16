def minimum_in_array():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    minimum = arr[0]
    for val in arr:
        if val < minimum:
            minimum = val

    print("Minimum:", minimum)

if __name__ == "__main__":
    minimum_in_array()
