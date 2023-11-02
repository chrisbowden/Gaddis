def main():
    my_string = input("Enter a string: ")


    # Init the space counter
    spaces = 0
    for ch in my_string:
        if ch.isspace():
            spaces += 1

    # Display the output
    print ("There are", spaces, "spaces in the string.")


main()