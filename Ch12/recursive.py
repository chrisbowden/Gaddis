# This program has a recursive function

def main():
    # By passing the argument 5 to the message
    # function we are telling it to display
    # the message 5 times

    message(9)

def message(times):
    if times > 0:
        print('This is a recursive function')
        message(times-1)

# Call main
main()
