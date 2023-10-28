# This program reads data from the sales file
# using loops and detects the end of file

def main():
    # Open the sales file
    sales_file = open("sales.txt", "r")

    # Read the first line, and test for empty strings
    line = sales_file.readline()

    # As long as empty string isn't returned, process
    # the line
    while line != "":
        # Convert line to a float
        amount = float(line)

        # Format and display the data
        print(format(amount, '.2f'))

        # Read the next line
        line = sales_file.readline()

    # Empty string found, so end of file. Close it.
    sales_file.close()


main()
