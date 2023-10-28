# Another gross pay calculator

def main():
    try:
        # Get hours worked and other data
        hours = int(input("How many hours did you work? "))
        pay_rate = float(input("Enter your hourly pay rate: "))

        gross_pay = hours * pay_rate

        print("Gross pay: $", format(gross_pay, ",.2f"), sep="")
    except ValueError as err:
        print(err)

main()
