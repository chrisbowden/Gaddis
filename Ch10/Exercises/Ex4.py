# Create the Employee Class
class Employee:
    def __init__(self, name, ID, dept, title):
        self.__name = name
        self.__IDNum = ID
        self.__dept = dept
        self.__title = title

    def __str__(self):
        return self.__name + "\t" + self.__IDNum + "\t" + self.__dept + "\t" + self.__title
    
    


def main():
    # Create a list to hold the objects as they are created
    employees = []

    # Create the first object
    user = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    # Add this user to the list
    employees.append(user)
    # Create the second object
    user = Employee("Mark Jones", "39119", "IT", "Programmer")
    employees.append(user)
    # Create the third object
    user = Employee("Joy Rogers", "47899", "Manufacturing", "Engineer")
    employees.append(user)

    # Loop through the list and print out each object
    for item in range (len(employees)):
        print(employees[item])


# Execute the main function
main()
