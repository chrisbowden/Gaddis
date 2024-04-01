# This program pickles CellPhone objects
import pickle
import cellphone

# Constant for the filename
FILENAME = 'cellphones.dat'

def main():
    # Init the variable to control the loop
    again = 'y'

    # Open a file
    output_file = open(FILENAME, 'wb')

    # Get data from the user
    while again.lower() == 'y':
        # Get the phone data
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))

        # Create the CellPhone object
        phone = cellphone.CellPhone(man, mod, retail)

        # Pickle the object and wrie it tp the file
        pickle.dump(phone, output_file)

        # Get more cell phone data?
        again = input('Enter more phone data? (y/n): ')

    # Close the file
    output_file.close()
    print('The data was written to', FILENAME)

# Call the main function()
main()

