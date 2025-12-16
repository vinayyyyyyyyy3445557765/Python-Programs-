def print_star_pattern():
    n = int(input("Enter number of rows: "))

    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

if __name__ == "__main__":
    print_star_pattern()
