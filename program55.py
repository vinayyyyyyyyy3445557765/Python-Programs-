def display_2d_array():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

if __name__ == "__main__":
    display_2d_array()
