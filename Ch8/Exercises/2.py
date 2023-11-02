# Enter a series of numbers and then sum them

def main():
    num = input("Enter a sequence of numbers: ")

    sum = 0

    for ch in num:
        sum += int(ch)

    print(sum)


main()