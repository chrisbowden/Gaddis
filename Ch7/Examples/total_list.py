# Calcs the total of values in a list

def main():
    # Create the list
    numbers = [2, 4, 6, 8, 10]

    # Create accumulator
    total = 0

    # Calc total of list elements
    for value in numbers:
        total += value

    # Display the totals
    print("The total of all elements is", total)


main()
