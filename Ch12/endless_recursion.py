# This is a demo of endless recursion

def main():
    message()

def message():
    print('This is a recursive function')
    message()

# Call main function
main()
