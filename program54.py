def binary_search():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    key = int(input("Enter element to search: "))

    low = 0
    high = n - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            found = True
            break
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print("Sorted Array:", arr)

    if found:
        print("Element found")
    else:
        print("Element not found")

if __name__ == "__main__":
    binary_search()
