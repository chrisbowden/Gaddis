# Program asks user to enter a number for the day of week
# Displays an error if the number is out of range

day = int(input("Enter a number for the day of the week (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("You entered an invalid number")
