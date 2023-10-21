# This program asks a user to enter a roulette number
# and displays if it is red, black or green

pocket = int(input("What is the pocket number? "))

if pocket % 2 == 0:
    even = True
else:
    even = False

if pocket == 0:
    colour = "Green"

if pocket >=1 and pocket <= 10:
    if even:
        colour = "Black"
    else:
        colour = "Red"

if pocket >=11 and pocket <= 18:
    if even:
        colour = "Red"
    else:
        colour = "Black"

if pocket >=19 and pocket <= 28:
    if even:
        colour = "Black"
    else:
        colour = "Red"

if pocket >=29 and pocket <= 36:
    if even:
        colour = "Red"
    else:
        colour = "Black"

print(colour)
