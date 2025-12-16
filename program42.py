def generate_alternating_series():
    n = int(input("Enter number of terms: "))
    value = 1
    sign = 1

    for i in range(n):
        print(sign * value, end=" ")
        value += 4
        sign *= -1

    print()

if __name__ == "__main__":
    generate_alternating_series()
