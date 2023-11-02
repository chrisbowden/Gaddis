# This progrm uses a dictionary to keep friends
# names and birthdays

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main function
def main():
    # Create the empty dictionary
    birthdays = {}

    # Init variable for user choice
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        # Process the choice
        if choice == LOOK_UP:
            look_up(birthdays)

        elif choice == ADD:
            add(birthdays)

        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete (birthdays)


# The get_menu_choice function displays the menu
# and gets a validated choice form the user
def get_menu_choice():
    print()
    print("Friends and Their Birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")
    print()

    # Get the user choice
    choice = int(input("Enter your choice: "))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    # Return the selection
    return choice

# Look up function
def look_up(birthdays):
    # Get the name to lookup
    name = input("Enter a name: ")

    # Look it up
    print(birthdays.get(name, "Not found."))

def add(birthdays):
    # Get a name and birthday
    name = input("Enter a name: ")
    bday = input("Enter a birthday: ")

    # If name doesnt exist, add it
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print("That entry already exists.")

def change(birthdays):
    # Get name to look up
    name = input("Enter a name: ")

    if name in birthdays:
        # Get the new birthday
        bday = input("Enter the new birthday: ")

        # Update the entry
        birthdays[name] = bday

    else:
        print("That name is not found.")

# Delete function
def delete(birthdays):
    name = input("Enter a name: ")

    if name in birthdays:
        del birthdays[name]
    else:
        print("That name is not found.")

# Call the main function
main()