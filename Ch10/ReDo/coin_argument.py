# THis program passes a coin object as
# an argument to a function
import coin

# Main Function
def main():
    # Create the coin object
    my_coin = coin.Coin()

    # THis wil display heads
    print(my_coin.get_sideup())

    # Pass the object to the flip function
    flip(my_coin)

    # This might display Heads or might Tails
    print(my_coin.get_sideup())

# The flip function flips a coin
def flip(coin_obj):
    coin_obj.toss()

# Define the mian function
main()
