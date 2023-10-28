# Sum of numbers found within the data file

def main():
    filename = input("Enter the filename you wish to display: ")

    # Open the file
    infile = open(filename, "r")

    # Init the sum / accumulator
    sum = 0

    # Read the first line
    line = infile.readline()

    # Now start processing the file line by line checking for
    # EOF / blank entries
    while line != "":
        try:
            line = float(line)
            sum += line
        except ValueError:
            pass
        line = infile.readline()

    infile.close()

    print("The total of all the entries is:", sum)


main()