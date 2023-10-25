# This program will calculate State and County
# Sales tax values

# Define some constants for the tax rates
STATE_TAX = 0.05
COUNTY_TAX = 0.025


def calc_tax(price, tax_rate):
    return price * tax_rate


def main():
    cost = float(input("Enter the value of the purchase: "))
    state = calc_tax(cost, STATE_TAX)
    county = calc_tax(cost, COUNTY_TAX)
    print("The totals are:")
    print()
    print("Cost:", cost)
    print("State Sales Tax:", state)
    print("County Sales Tax:", county)
    print("Total:", cost+state+county)

main()