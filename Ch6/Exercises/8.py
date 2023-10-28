# Sum of numbers found within the data file

def main():
    FILENAME = "random_nums.txt"

    # Open the file
    infile = open(FILENAME, "r")

    # Init the sum / accumulator
    sum = 0
    count = 0

    # Read the first line
    line = infile.readline()

    # Now start processing the file line by line checking for
    # EOF / blank entries
    while line != "":
        try:
            line = float(line)
            sum += line
            count += 1
        except ValueError:
            pass
        line = infile.readline()

    infile.close()

    print("The total of all the entries is:", sum)
    print("The number of random numbers is:", count)

main()