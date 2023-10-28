def main():

    filename = input("Enter the filename: ")
    infile = open(filename, "r")
    for line in infile:
        line = line.rstrip("\n")
        print(line)
    infile.close()
main()
