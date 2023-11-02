# Get the user's name
# and display their initials

def main():
    my_name = input("Enter your full name: ")

    # Lets assume the fist letter is preceded by a space
    my_initials = my_name[0] + "."

    for i in range(len(my_name)):
        if my_name[i] == " ":
            my_initials += my_name[i+1] + "."

    print(my_initials)

main()