# Larger than n
# Function accepts two arguments, a list and a number
# Display all the numbers in the list greater than n

def main():
    # Create the list to be used for comparisons
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    num_check = int(input("Enter a number to compare: "))

    greater_n(numbers, num_check)




def greater_n(numberlist, check_num):
    for item in numberlist:
        if item > check_num:
            print(item)






main()

