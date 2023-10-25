# Program generates two random numbers between 0 and 200
# and asks user to add them together
import random
MIN=1
MAX=300

def get_number():
    return random.randint(MIN,MAX)

def sum(num1, num2):
    return num1 + num2

def main():
    print ("This program will display two numbers and you")
    print("should add them together.")
    print()
    first = get_number()
    second = get_number()
    total = sum(first,second)
    print(" ", first)
    print("+", second)
    answer = int(input("What is your answer? "))
    if answer == total:
        print("Congratulations, you are correct!")
    else:
        print ("Sorry, that is incorrect.")

main()
