# This program demonstrates the insert method

def main():
    # Create list with some names
    names = ["James","Kathryn", "Bill"]

    # Display the list
    print("The list before the insert:")
    print(names)

    # Insert a new name at element 0
    names.insert(0, "Joe")

    # Display the list again
    print("The list after the insert:")
    print(names)

main()

