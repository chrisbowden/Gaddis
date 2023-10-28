# Ask user for filename, and open it for reading
# catch error if file not found

def main():
    try:
        # Ask user for filename
        filename = input("Enter the filename: ")

        infile = open(filename, "r")
        data = infile.read()

        infile.close()

        print(data)
    except IOError:
        print("The file cannot be found, so creating it")
        outfile = open(filename, "w")
        outfile.close()

main()
