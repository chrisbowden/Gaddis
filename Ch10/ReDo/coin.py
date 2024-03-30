import random
# The coin class simulates a coin that can be flipped

class Coin:

    # The __init__ method initialises the 
    # sideup data attribute with heads

    
    # I guess this is the constructor??
    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range 0 through 1. If the number is
    # 0 then the sideup is set to 'Heads'.
    # Otherwise sideup is set to 'Tails'

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method retunrs the value of the coin

    def get_sideup(self):
        return self.__sideup