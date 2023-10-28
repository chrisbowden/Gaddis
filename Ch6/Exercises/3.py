# Print the contents of a text file
# including the line number

def main():
    filename = input("Enter the filename you wish to display: ")

    # Open the file
    infile = open(filename, "r")

    # init a counter to use as the line number
    lineNum = 1

    # Read the first line
    line = infile.readline()

    # Now start processing the file line by line checking for
    # EOF / blank entries
    while line != "":
        line = line.rstrip("\n")
        print(str(lineNum) + ": " + line)
        lineNum += 1
        line = infile.readline()

    infile.close()


main()