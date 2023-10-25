# This program simulates rolling of dice
import random

# Constants for min and max random numbers
MIN = 1
MAX = 6


def main():
    # Create variable to control the loop
    again = 'y'

    # Simulate rolling the dice
    while again == 'y' or again == 'Y':
        print("Rolling the dice ...")
        print("Their values are:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Do another roll?
        again = input("Roll them again? (y = yes): ")


main()
