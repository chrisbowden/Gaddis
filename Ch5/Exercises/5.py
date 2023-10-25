# Define the constant for the assessment value
ASSESS_RATE = 0.60

def main():
    property_value = float(input("Enter the property value: "))
    assess = assess_value(property_value)
    print("The assessment value is $", assess)
    print("The property tax will be $", format(calc_tax(assess), ',.2f'))

def assess_value(cost):
    return cost * ASSESS_RATE

def calc_tax(value):
    tax = value / 100 * 0.72
    return tax

main()
