def matrix_transpose():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    print("Matrix:")
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

    print("Transpose:")
    for j in range(c):
        for i in range(r):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    matrix_transpose()
