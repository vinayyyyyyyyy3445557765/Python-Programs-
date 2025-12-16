def reverse_array():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    reversed_arr = []

    for i in range(n - 1, -1, -1):
        reversed_arr.append(arr[i])

    print("Reversed Array:", reversed_arr)

if __name__ == "__main__":
    reverse_array()
