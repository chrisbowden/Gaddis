# Simulation of 10 coin tosses
import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Simulate coin tosses
        if random.randint(HEADS,TAILS) == HEADS:
            print("Heads.")
        else:
            print("Tails.")


main()