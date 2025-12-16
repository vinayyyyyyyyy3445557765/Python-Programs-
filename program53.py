def sort_array():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    choice = input("Enter A for Ascending or D for Descending: ")

    for i in range(n):
        for j in range(i + 1, n):
            if (choice == 'A' or choice == 'a') and arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            if (choice == 'D' or choice == 'd') and arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print("Sorted Array:", arr)

if __name__ == "__main__":
    sort_array()
