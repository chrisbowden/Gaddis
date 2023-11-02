# Get a string and remove all consanents

def main():
    my_string = input("Enter a string: ")

    new_string = ""
    for ch in my_string:
        if ch in ["a", "e", "i", "o" , "u"]:
            new_string += ch

    print(new_string)


main()
