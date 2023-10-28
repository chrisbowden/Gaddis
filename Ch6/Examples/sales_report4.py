# Program to display totals in sales data file

def main():
    # init the accumulator
    total = 0.0

    try:
        # Open sales data file
        infile = open("sales_data.txt")

        # Read the file
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()


    except Exception as err:
        print(err)

    else:
        # print totals
        print(format(total, ",.2f"))


main()
