def print_increasing_star_pattern():
    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":
    print_increasing_star_pattern()
