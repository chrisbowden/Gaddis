# program to calculate total cost of a meal

meal_cost = float(input("What is the cost of your meal? "))
tip = meal_cost * 0.18
tax = meal_cost * 0.07
print("Meal Cost:\t", format(meal_cost,'4.2f'))
print("Tip:\t\t", format(tip, '4.2f'))
print("Tax:\t\t", format(tax, '4.2f'))
print()
print("Total:\t\t", format(meal_cost+tip+tax, '4.2f'))