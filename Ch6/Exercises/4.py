# Count the number of items in a datafile

FILENAME = "numbers1.txt"


def main():
    # Open the file
    infile = open(FILENAME, "r")

    # Init a counter (start at zero in case the file is actually empty
    counter = 0

    # Read first item
    line = infile.readline().rstrip("\n")

    while line != "":
        counter += 1
        line = infile.readline()

    infile.close()
    print("The number of items found is the datafile was:", counter)


main()
