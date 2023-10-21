# User enters a series of positive numbers
# and we will display the sum. If they enter
# a negative number, we finish entering numbers

sum = 0 # Init the acucmulator
number = 1 # Init a dummy variable to ensure the loop runs at least 1 time
while number >=0:
    number = int(input("Enter a number to add (-ve number to end): "))
    if number >=0:
        sum += number

# If you get here, it means the loop has finished due to -ve number entered
print("The total of the numbers you entered is:", sum)
