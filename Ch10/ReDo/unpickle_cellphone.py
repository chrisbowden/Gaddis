# THis progrma unpickles CellPhone objects
import pickle
import cellphone

# Constant for the file name
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False     # To indicate the end of file

    # Open the file
    input_file = open(FILENAME, 'rb')

    # Read to the end of the file
    while not end_of_file:
        try:
            # Unpickle the next object
            phone = pickle.load(input_file)

            # Display the cell phone data
            display_data(phone)

        except EOFError:
            # Set the flag to indicate the end of the file
            # has been reached
            end_of_file = True
    
    # Close the file
    input_file.close()

# The display_data function displays the sata
# from the CellPhoen object passed as an argument
    
def display_data(phone):
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')
    print()

# Call the main function
main()
