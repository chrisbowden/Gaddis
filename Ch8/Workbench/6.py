# Accept a string and returns true if
# contains an @ symbol
def main():
    my_string = input("Enter the email address: ")

    # Check it
    if check_string(my_string):
        print("Valid")
    else:
        print("Not valid")


def check_string(email):
    if "@" in email:
        return True
    else:
        return False



main()