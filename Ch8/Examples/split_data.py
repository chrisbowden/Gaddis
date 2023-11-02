# This program calls the split method
# using the '/' character as the separator

def main():
    # Create a string with a date
    date_string = "11/26/2014"

    # Split the data
    date_list = date_string.split("/")

    # Display each piece of the data
    print("Month:", date_list[0])
    print("Day:", date_list[1])
    print("Year:", date_list[2])


main()
