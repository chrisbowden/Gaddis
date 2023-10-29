# Calcs the average of values in a list

def main():
    # Create the list
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # Create accumulator
    total = 0

    # Calc total of list elements
    for value in scores:
        total += value

    # Calculate the averagre
    average = total / len(scores)

    # Display the totals
    print("The average of the elements is", average)


main()
