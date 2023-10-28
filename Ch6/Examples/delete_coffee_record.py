# Program to allow user to delete a record

import os


def main():
    # Create flag variable
    found = False

    # Capture coffee to delete
    search = input("Which coffee do you wish to delete? ")

    # Open the original coffee file and create temp file
    coffee_file = open("Coffee.txt", "r")
    temp_file = open("temp.txt", "w")

    # Grab first record
    descr = coffee_file.readline()

    # Read the rest
    while descr != "":
        qty = float(coffee_file.readline())
        descr = descr.rstrip("\n")

        # If this is not the record to delete, write it
        # to the temp file
        if descr != search:
            # Write this record to the temp file
            temp_file.write(descr + "\n")
            temp_file.write(str(qty) + "\n")
        else:
            # set flag to True
            found = True

        # Next record
        descr = coffee_file.readline()

    # Close the files
    coffee_file.close()
    temp_file.close()

    # Delete old file and rename
    os.remove("coffee.txt")
    os.rename("temp.txt", "coffee.txt")

    # Display messages to indicate success or not
    if found:
        print("The file has been updated")
    else:
        print("That item was not found in the file")


main()
