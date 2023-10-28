# Program to write three lines of data
def main():
    # Open a file for writing
    outfile = open("philosophers.txt", "w")

    # Write some names to the file
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    # Close the file
    outfile.close()

main()
