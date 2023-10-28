# Writes three names to a file

def main():
    print("Enter the names of three people: ")
    name1 = input("Person #1: ")
    name2 = input("Person #2: ")
    name3 = input("Person #3: ")

    # Open a file for writing
    myfile = open("friends.txt", "w")

    # Write the names to the file
    myfile.write(name1 + "\n")
    myfile.write(name2 + "\n")
    myfile.write(name3 + "\n")

    # Close the file
    myfile.close()
    print("Names were written to friends.txt")

main()