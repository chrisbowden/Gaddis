# Program that allows user to search for records matching a description

def main():
    # Create a boolean to act as a flag
    found = False

    # Get the search value
    search = input("Enter a description to search for: ")

    # Open the coffee file
    coffee_file = open("coffee.txt", "r")

    # Read the first record / field
    descr = coffee_file.readline()

    # read the rest of the file (if needed)
    while descr != "":
        # Read quantity field
        qty = float(coffee_file.readline())

        # Strip the newlines
        descr = descr.rstrip("\n")

        # Does the record match the search value?
        if descr == search:
            print("Description:", descr)
            print("Quantity:", qty)
            print()
            # Set found flag to true
            found = True
        # Read the next description
        descr = coffee_file.readline()

    # Close the file
    coffee_file.close()

    # If the search value wasn't found, display a message
    if not found:
        print("That item was not found in the file.")


main()
