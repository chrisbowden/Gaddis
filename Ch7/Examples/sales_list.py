# Grabs data from user and stores in a list

NUM_DAYS = 5

def main():
    # Create list to hold sales data
    sales = [0] * NUM_DAYS

    # Variable to hold an index
    index = 0

    print("Enter the sales for each day.")

    # Get the sales for each day
    while index < NUM_DAYS:
        print("Day #", index +1, ": ", sep="", end="")
        sales[index] = float(input())
        index += 1

    # Display vales entered
    print("Here are the values youe entered:")
    for value in sales:
        print(value)

main()
