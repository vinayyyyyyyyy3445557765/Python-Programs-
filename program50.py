def count_odd_even():
    n = int(input("Enter size of array: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    odd = 0
    even = 0

    for val in arr:
        if val % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even count:", even)
    print("Odd count:", odd)

if __name__ == "__main__":
    count_odd_even()
