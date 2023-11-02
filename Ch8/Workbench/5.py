# Accept a string and returns true if
# ends with .com

def main():
    my_string = input("Enter the email address: ")

    # Check it
    if check_string(my_string):
        print("Valid")
    else:
        print("Not valid")


def check_string(email):
    if email.endswith(".com"):
        return True
    else:
        return False



main()