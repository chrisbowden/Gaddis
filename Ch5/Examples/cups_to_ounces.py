# This program converts cups to fluid ounces

def main():
    # Display intro screen
    intro()
    # Get the number of cups
    cups_needed = int(input("Enter the number of cups: "))
    cups_to_ounces(cups_needed)


def intro():
    print("This program converts measurements")
    print("in cups to fluid ounces. For your")
    print("the formula is:")
    print(" 1 cup = 8 fluid ounces")
    print()


def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")


# Call main
main()
