# This program imports the coin module and
# creates an instance of the Coin class

import coin

def main():
    # Create object from coin class
    my_coin = coin.Coin()

    # Display the up side
    print("This side is up:", my_coin.get_sideup())

    # Toss
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call main
main()
