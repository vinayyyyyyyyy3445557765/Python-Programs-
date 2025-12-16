def print_number_pattern():
    n = int(input("Enter number of rows: "))

    for i in range(n):
        for j in range(1, n + 1):
            print(j, end="")
        print()

if __name__ == "__main__":
    print_number_pattern()
