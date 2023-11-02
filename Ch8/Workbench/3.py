# Count upper and lowercase characters in a string

def main():
        my_string = input("Enter a string: ")

        # Init counters
        upper = 0
        lower = 0

        for ch in my_string:
            if ch.islower():
                lower += 1
            if ch.isupper():
                upper += 1

        print("There were:", lower, "lowercase characters")
        print ("and", upper, "uppercase characters.")


main()