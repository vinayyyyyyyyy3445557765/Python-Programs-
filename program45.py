def store_array_elements():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    print(arr)

if __name__ == "__main__":
    store_array_elements()
