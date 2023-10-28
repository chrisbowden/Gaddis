# Prompt the user for sales amounts
# and process via a loop

def main():
    # Get the number of days
    num_days = int(input("For how many days do you have sales? "))

    # Open a new file
    sales_file = open("sales.txt", "w")

    # get amount for each day and write to file
    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for day #" + str(count) + ": "))

        # Write the sales amounts
        sales_file.write(str(sales) + "\n")

    # Close the file
    sales_file.close()
    print("Data written to sales.txt")


main()
