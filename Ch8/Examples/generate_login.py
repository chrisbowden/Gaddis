# Generate Login gets the users name

import login

def main():
    # get user's first name, last and ID
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your Student ID number: ")

    # Get the login name
    print("Your system login name is:")
    print(login.get_login_name(first, last, idnumber))

main()