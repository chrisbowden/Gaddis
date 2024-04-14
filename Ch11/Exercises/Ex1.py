# This progrm utilises the Exployee class (Ex1)
# To create an object and replay the data

import employee

def main():


    # Collect the required data
    name = input("Enter the employee name: ")
    number = input('Enter the employee number: ')
    shift = input ('Enter the correct shift (1 or 2): ')
    pay = float(input('Enter the pay rate: '))

    # Create the object 
    prodworker = employee.ProductionWorker(name, number, shift, pay)

    # Output the details
    print("Here are the details for the employee:")
    print()
    print('Employee Name: ', prodworker.get_emp_name())
    print('Employee Number: ', prodworker.get_emp_number())
    print('Shift: ', prodworker.get_shift())
    print('Pay Rate: ', prodworker.get_pay_rate())
    


# Run the main function
main()