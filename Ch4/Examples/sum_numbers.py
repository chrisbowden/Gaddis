# This program calculates the sum of a series of numbers
max = 5

# Init the accumulator
total = 0

print("This program calculates the sum of")
print(max, "numbers you will enter")

# get the numbers and accumulate them
for counter in range(max):
    number = int(input("Enter a number: "))
    total = total + number

print("The total is", total)
