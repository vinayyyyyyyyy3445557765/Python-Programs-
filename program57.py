def search_2d_array():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    key = int(input("Enter element to search: "))
    found = False

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == key:
                found = True

    if found:
        print("Element found")
    else:
        print("Element not found")

if __name__ == "__main__":
    search_2d_array()
