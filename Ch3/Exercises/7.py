# Asks user to enter two primary colours and determines
# the resulting colour. Displays error is incorrect
# colours entered

colour1 = input("Enter the first colour: ")
colour2 = input("Enter the second colour: ")

if (colour1 == "red" and colour2 == "blue") or (colour1 == "blue" and colour2 == "red"):
    print("You get purple.")

elif (colour1 == "red" and colour2 == "yellow") or (colour1 == "yellow" and colour2 == "red"):
    print("You get orange.")

elif (colour1 == "blue" and colour2 == "yellow") or (colour1 == "yellow" and colour2 == "blue"):
    print("You get green.")

else:
    print("You entered an invalid colour")
