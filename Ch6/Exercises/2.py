# This is a python implementation of a 'head' program
# Display the first 5 lines of a data file
# and if less than 5 lines, just what is there

FILENAME = "numbers.txt"

def main():
    # Open the file for reading
    infile = open(FILENAME, "r")

    for i in range(5):
        line = infile.readline()
        if line != "":
            line = line.rstrip("\n")
            print(line)


    infile.close()

main()
