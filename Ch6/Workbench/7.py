import os

def main():
    infile = open("students.txt", "r")
    outfile = open("temp.txt", "w")

    found = False

    # Read the first field from first record
    name = infile.readline()

    # Read through the file (looking for EOF as well)
    while name != "":
        score = float(infile.readline())
        name = name.rstrip("\n")

        if name == "John Perz":
            found = True
        else:
            # In this instance write the data to the new file
            outfile.write(name + "\n")
            outfile.write(str(score) + "\n")

        # Next record
        name = infile.readline()

    # At this stage we have read through all the records, so close out the files
    infile.close()
    outfile.close()
    os.remove("students.txt")
    os.rename("temp.txt", "students.txt")
    if not found:
        print("The selected record was not found")
    else:
        print("Record was deleted!")

main()

