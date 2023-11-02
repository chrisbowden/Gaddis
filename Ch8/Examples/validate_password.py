# Program gets password from user and validates it

import login

def main():
    # Get password from the user
    password = input("Enter your password: ")

    # Validate password
    while not login.valid_password(password):
        print("That password is not valid.")
        password = input("Enter your password: ")

    print("That is a valid password")


main()