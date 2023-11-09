import random

# The class simulates a coin that can be flipped


class Coin:

    # The __init__ method initialises the sideup data
    # with Heads

    def __init__(self):
        self.sideup = "Heads"

    # The toss method generates a random number
    # If 0, it is heads, if 1, tails



    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    # The get sideup method returns the value


    def get_sideup(self):
        return self.sideup

# The main function
def main():
    # Create an object from the Coin class
    my_coin = Coin()

    # Display the current state
    print("This side is up:", my_coin.get_sideup())

    # Toss the coin
    print("I am tossing the coin . . . ")
    my_coin.toss()

    # But now I am goig ot cheat. I'm going to
    # directly change the value of the object's
    # sideup attribute to Heads
    my_coin.sideup = "Heads"

    # Display the current state
    print("This side is up:", my_coin.get_sideup())

# Call main
main()