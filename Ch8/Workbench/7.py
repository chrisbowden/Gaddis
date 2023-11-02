# Look for first occurance of a vowel and replace it with an X
def main():
    my_string = input("Enter a sentence: ")

    # Set a sentinal for Vowel already found
    vowel_found = False

    # Create a new string as the output
    new_string = ""

    for ch in my_string:
        if not vowel_found and ch in ["a", "e", "i", "o", "u"]:
            new_string += "X"
            vowel_found = True
        else:
            new_string += ch


    print(my_string)
    print(new_string)

main()