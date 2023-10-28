# Program to display contents of a file

def main():
    # Get the name of a file
    filename = input("Enter a filename: ")

    # Open the file
    infile = open(filename, "r")

    # Read the contents
    contents = infile.read()

    # Display the contents
    print(contents)

    # Close the file
    infile.close()


main()