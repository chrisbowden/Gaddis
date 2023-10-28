# Read files line by line
def main():
    # Open a file
    infile = open("philosophers.txt", "r")

    #Read the three lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close file
    infile.close()

    # Print the data
    print(line1)
    print(line2)
    print(line3)

   

main()