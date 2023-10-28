# Program to read from a file

def main():
    # Open a file
    infile = open("philosophers.txt", "r")

    # Read the contents
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Display the contents we read in
    print(file_contents)

main()
