# Program to generate a user specified number of random numbers
# and write them to a data file
import random

FILENAME = "random_nums.txt"

def main():
    # Ask the user how manu numbers to generate
    num_ints = int(input("How many random numbers would you like to generate? "))

    # Open the file for writing
    outfile = open(FILENAME, "w")

    for i in range(num_ints):
        number = random.randint(1,500)
        outfile.write(str(number)+ "\n")



    outfile.close()

main()