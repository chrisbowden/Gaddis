# Display the records in the coffee file
def main():
    coffee_file = open("coffee.txt","r")

    # Read 1st record and check EOF
    descr = coffee_file.readline()

    while descr != "":
        qty = float(coffee_file.readline())

        # Strip newlines
        descr = descr.rstrip("\n")

        # Display the records
        print("Description:", descr)
        print("Quantity:", qty)

        # Next record
        descr = coffee_file.readline()

    coffee_file.close()

main()