def matrix_multiplication():
    r1 = int(input("Enter rows of first matrix: "))
    c1 = int(input("Enter columns of first matrix: "))
    r2 = int(input("Enter rows of second matrix: "))
    c2 = int(input("Enter columns of second matrix: "))

    if c1 != r2:
        print("Matrix multiplication not possible")
        return

    A = []
    B = []

    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"Enter A[{i}][{j}]: ")))
        A.append(row)

    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"Enter B[{i}][{j}]: ")))
        B.append(row)

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        for val in row:
            print(val, end=" ")
        print()

if __name__ == "__main__":
    matrix_multiplication()
