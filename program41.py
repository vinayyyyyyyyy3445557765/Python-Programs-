def number_to_words():
    num = int(input("Enter number: "))
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []

    while num > 0:
        digit = num % 10
        result.append(words[digit])
        num //= 10

    for word in reversed(result):
        print(word, end=" ")

    print()

if __name__ == "__main__":
    number_to_words()
