# This program generates 100 random numbers, determines if
# each number is odd or even, and counts them
import random


def iseven(number):
    if number%2 == 0:
        return True
    else:
        return False

def main():
    even_count=0
    odd_count=0
    for i in range(100):
        random_number = random.randint(1,100)
        if iseven(random_number):
            even_count += 1
        else:
            odd_count += 1

    print("The total number of even numbers was:", even_count)
    print("The total number of odd numbers was:", odd_count)


main()