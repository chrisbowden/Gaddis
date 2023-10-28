def main():

    # Init the accumulator
    total = 0.0

    filename = input("Enter the filename: ")
    infile = open(filename, "r")
    for line in infile:
        line = line.rstrip("\n")
        print(line)
        total += int(line)
    infile.close()
    print("The total for the numbers is:", total)
main()