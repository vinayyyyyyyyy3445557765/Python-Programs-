def search_element():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    key = int(input("Enter element to search: "))

    found = False
    for val in arr:
        if val == key:
            found = True
            break

    if found:
        print("Element found")
    else:
        print("Element not found")

if __name__ == "__main__":
    search_element()
