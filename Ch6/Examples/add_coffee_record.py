# Program to append records in the coffee file

def main():
    # Create loop control variable
    another = "y"

    # Open the file
    coffee_file = open("coffee.txt", "a")

    # Add records
    while another == "y" or another == "Y":
        # Get the record data
        print("Enter the following coffee data:")
        descr = input("Description: ")
        qty = int(input("Quantity (in pounds): "))

        # Append the data
        coffee_file.write(descr + "\n")
        coffee_file.write(str(qty) + "\n")

        # Determine if user wants to add another record
        print("Do you want to add another record?")
        another = input("Y = yes, anything else = no: ")

    # close the file
    coffee_file.close()

main()
