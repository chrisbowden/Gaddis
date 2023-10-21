# Displays a table of numbers and their squares
# based on user limit

# Get the ending limit
print("This program displays a list of numbers")
print ("(starting at 1) and their squares.")

# Get a staring number
start = int(input("Enter the starting number: "))


end = int(input("How high should I go? "))

# Print the table headings
print()
print("Number\tSquare")
print("---------------")

# Print the numbers and their squares
for number in range(start, end+1):
    square = number**2
    print(number, '\t\t', square)
