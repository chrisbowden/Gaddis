# Generate a random 7 digit lottery number
import random

def main():
    # Create the basic list
    numbers = []

    # Create a loop that runs 7 times (1 per number) and generates
    # one entry each time in the list

    for i in range(7):
        random_num = random.randint(0,9)
        numbers.append(random_num)

    print(numbers)

    print("The lottery number is:")
    print()

    for item in numbers:
        print(item, sep='',end='')
    print()

    
main()