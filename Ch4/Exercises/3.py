# Init the sentinal
expense=1

# Init the expenses total
exp_total = 0

budget = float(input("What is your budget for the month? "))

while expense!= 0:
    expense = float(input("Enter your expense (0 to finish): "))
    exp_total += expense

net = budget - exp_total
if net > 0:
    print("You are under budget by $", net, sep='')

elif net < 0:
    print("You are over budget by $", net, sep='')

else:
    print("You are right on budget")

