# Uses append method for adding item to list

def main():
    # Create an empty list
    name_list = []

    # Create loop control variable
    again = 'y'

    # Add some names
    while again == 'y':
        # Get a name from the user
        name = input("Enter a name: ")

        # Append to the list
        name_list.append(name)

        # Add another?
        print("Do you want to add another name?")
        again = input("y = yes, anything else = no: ")
        print()

    # Display the names entered
    print("Here are the names you entered.")

    for name in name_list:
        print(name)


main()
