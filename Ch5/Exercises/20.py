# This is a random number guessing game
import random

def main():
    num = get_random()
    guess_count = 0
    correct = False
    while correct != True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1
        correct = check_num(user_guess, num)
    print("You guessed it! It took", guess_count, "guesses.")


def get_random():
    return random.randint(1,100)

def check_num(guess, num):
    if guess > num:
        print("Your guess is too high")

    elif guess < num:
        print("Your guess is too low")
    else:
        return True


main()