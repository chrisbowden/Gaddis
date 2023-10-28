# Read data from a file line by line
# and remove the line breaks

def main():
    # Open a file
    infile = open("philosophers.txt","r")

    # Read the lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Strip off the newline characters
    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")

    # Close file
    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()