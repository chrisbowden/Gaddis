# Calculate pay if the user earns 1 penny on day 1
# 2 pennies on day 2 etc

total = 0 # Init the intial pay value
num_days = int(input("How many days do you want to calculate: "))
for num_pennies in range(num_days):
    total += (num_pennies+1)

print("The total value of the pennies after ",num_days, " days will be $", total/100, sep='' )