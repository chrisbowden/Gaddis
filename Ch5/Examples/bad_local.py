# Definition of main function
def main():
    get_name()
    print("Hello", name) # This will cause an error

# Get name function
def get_name():
    name = input("Enter your name: ")

# Call main
main()
