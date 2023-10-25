# Calculator for insurance

# Define the minimum rate of insurance cover
MIN_RATE = 0.80

def main():
    cost = float(input("Enter the replacement cost for the building: "))
    ins_value = calc_insurance(cost)
    print("The minimum insurance value should be $", ins_value, sep='')

def calc_insurance(num):
    return num * MIN_RATE

main()