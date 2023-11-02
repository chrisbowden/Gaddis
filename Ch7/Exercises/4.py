# Capture 20 numbers
# then display total, average and min/max entries

def main():

    numbers = []
    print("Enter 20 numbers.")
    print()
    for i in range(20):
        print("Enter number #", i+1, ": ", sep='',end='')
        number = int(input())
        numbers.append(number)


    total = 0
    for item in numbers:
        total += item

    max_value = max(numbers)
    min_value = min(numbers)
    average = total / len(numbers)

    print("The total of the numbers is: ", total)
    print("The average is: ", average)
    print("The maximum is: ", max_value)
    print("The minimum is: ", min_value)

main()