# Determines if user chosen date is a magic date
# where the month * day is same as the year

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year (two digits): "))

if day * month == year:
    print("This is a magic date!")
else:
    print("Sorry, no magic here :-(")
