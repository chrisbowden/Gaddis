# Program to read the records saved in the employee file

def main():
    # Open the file
    emp_file = open("employees.txt", "r")

    # Read the first line and check for empty string
    name = emp_file.readline()

    # Check for EOF (empty string)
    while name != "":
        # Read id number
        id_num = emp_file.readline()
        dept = emp_file.readline()

        # Strip the newline characters
        name = name.rstrip("\n")
        id_num = id_num.rstrip("\n")
        dept = dept.rstrip("\n")

        # Display the record
        print("Name:", name)
        print("ID:", id_num)
        print("Dept:", dept)
        print()

        # Read the next record
        name = emp_file.readline()

    # Close the file
    emp_file.close()


main()
