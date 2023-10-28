# This program allows user to modify the quantity
# in a record

import os  # Used for file removal and rename functions


def main():
    # Create a bool variable to use as a flag
    found = False

    # Capture search value
    search = input("Enter a description to search for: ")
    new_qty = int(input("Enter the new quantity: "))

    # Open the data file
    coffee_file = open("coffee.txt", "r")

    # Create / open a temp file
    temp_file = open("temp.txt", "w")

    # Read the first record
    descr = coffee_file.readline()

    # Continue reading of not EOF
    while descr != "":
        qty = float(coffee_file.readline())

        # Strip newlines
        descr = descr.rstrip("\n")

        # Either write this unmatched to the temp file,
        # or write a new record is matched
        if descr == search:
            temp_file.write(descr + "\n")
            temp_file.write(str(new_qty) + "\n")

            # Set the found flag as record matches
            found = True

        else:
            # Write the original record to temp file
            temp_file.write(descr + "\n")
            temp_file.write(str(qty) + "\n")

        # Read the next record
        descr = coffee_file.readline()

    # Close the data files
    coffee_file.close()
    temp_file.close()

    # Remove the original file
    os.remove("coffee.txt")

    # rename the temp file
    os.rename("temp.txt", "coffee.txt")

    # if the search value was not found display a message
    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file.")


main()
