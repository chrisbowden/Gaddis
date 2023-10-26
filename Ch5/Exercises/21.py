# Game of rock paper and scissors
import random

def get_random():
    selected = random.randint(1,3)
    return selected

def main():
    # Start with the computer selecting
    game_over = 0
    while game_over == 0:
        AI_Choice = get_random()
        print(AI_Choice)
        user_choice = input("Choose Rock, Paper or Scissors: ").upper()
        usernum = convert_choice(user_choice)

        # Evaluate the user and AI choices
        # If the return value = 0, AI wins
        # If the return value is 1, User wins
        # If return value = 2, it was a draw
        winner = find_winner(usernum, AI_Choice)
        if winner == 2:
            print("It was a draw. Play again.")
            continue
        elif winner == 0:
            print("Computer Wins!")
        else:
            print("User Wins!")
        game_over = 1



def convert_choice(user):
    if user == "ROCK":
        return 1
    elif user == "PAPER":
        return 2
    else:
        return 3

def find_winner(usernum, AIChoice):
    if usernum > AIChoice:
        if usernum == 3 and AIChoice == 1:
            return 0
        else:
            return 1
    elif usernum == AIChoice:
        return 2
    else:
        if usernum == 1 and AIChoice == 3:
            return 1
        else:
            return 0

main()