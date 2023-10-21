# Demo of two functions that have local variables
# with the same name

def main():
    # Call the texas function
    texas()
    # Call the california function
    california()


# Definition of the Texas function
def texas():
    birds = 5000
    print("Texas has", birds, "birds.")


def california():
    birds = 8000
    print("California has", birds, "birds.")

main()
