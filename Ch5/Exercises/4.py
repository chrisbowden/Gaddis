

def main():
    print("Please enter monthly values for the following vehicle expenses:")
    repayment = float(input("Loan Repayment: "))
    insurance = float(input("Insurance: "))
    gas = float(input("Gas: "))
    oil = float(input("Oil: "))
    tyres = float(input("Tyres: "))
    maintenance = float(input("Maintenance: "))
    monthly_total = repayment+insurance+gas+oil+tyres+maintenance
    yearly_total = yearly(monthly_total)

    print("The monthly total is $", monthly_total, sep='')
    print("The yearly total is $", yearly_total, sep='')

def yearly(value):
    return value*12

main()