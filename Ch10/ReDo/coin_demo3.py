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

# The main functino starts here
def main():
    # Create an object from the Coin class
    my_coin = Coin()

    # Display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin
    print('I am tossing the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


# Call the main function
main()