# Allows a user to enter a non negative number
# and will display the factorial of that number
number = int(input("Please enter a non negative number: "))
factorial = 1 # The initial value for the factorial

for i in range(number, 0, -1):
    factorial *= i

print(number, "! is ", factorial, sep='')