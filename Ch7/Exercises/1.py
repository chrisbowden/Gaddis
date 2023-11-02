# Calculates total sales

def main():
    # Create an empty list
    sales = []
    total = 0

    # Loop through and capture 5 days of sales
    # and pop them in the list
    for i in range(5):
        print("What are the sales for day #", i+1, ": ", sep='', end='')
        daily_sales = float(input())
        sales.append(daily_sales)
    for item in sales:
        total += item

    print("The total sales for the week is $", total, sep='')
    






main()