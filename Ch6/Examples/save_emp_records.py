# Program to get employee data and saves as records

def main():

    # Get the number of employees
    num_emps = int(input("How many employee records do you wish to create? "))

    # Open the file
    emp_file = open("employees.txt", "w")

    # Get each employees data
    for count in range(1, num_emps+1):
        print("Enter data for employee #",  count, sep='')
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")

        # Write the data to the file
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")

        # Display blank line
        print()

    # Close the file
    emp_file.close()
    print("Employee records written to employees.txt")

main()
