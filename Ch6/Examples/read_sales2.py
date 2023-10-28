# This reads the sales file like the previous program, but uses
# a for loop to auto detect EOF

def main():
    # Open the file
    sales_file = open("sales.txt", "r")

    # Read all the lines
    for line in sales_file:
        # Convert line to a float
        amount = float(line)
        print(format(amount, ',.2f'))

    # Close the file
    sales_file.close()


main()
