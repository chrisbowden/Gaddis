

def main():
    infile = open("numbers.txt", "r")

    # Get three numbers
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    # Add the numbers
    total = num1+num2+num3
    print("The numbers are:", num1, num2, num3)
    print("The total is:", total)
    

main()
