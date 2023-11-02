# Demo of object unpickling
import pickle

# Main function
def main():
    end_of_file = False

    # Open file for binary reading
    input_file = open('info.dat', 'rb')

    # Read to end of file
    while not end_of_file:
        try:
            # Unpickle the next object
            person = pickle.load(input_file)
            # Display the object
            display_data(person)
        except EOFError: # Set flag to indicate EOF has been reached
            end_of_file = True

    # Close the file
    input_file.close()

# The diaplsy data function
def display_data(person):
    print("Name: ", person["name"])
    print("Age: ", person["age"])
    print("Weight: ", person["weight"])
    print()

main()
