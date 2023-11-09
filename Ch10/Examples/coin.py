import random


# The class simulates a coin that can be flipped


class Coin:

    # The __init__ method initialises the sideup data
    # with Heads

    def __init__(self):
        self.__sideup = "Heads"

    # The toss method generates a random number
    # If 0, it is heads, if 1, tails

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    # The get sideup method returns the value

    def get_sideup(self):
        return self.__sideup
