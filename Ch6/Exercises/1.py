FILENAME = "numbers.txt"

def main():
    infile = open(FILENAME, "r")
    for line in infile:
        print(line.rstrip("\n"))

    infile.close()

main()
