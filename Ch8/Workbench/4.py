# Ask user to enter a 5 digit number
# and print the sum

def main():
    my_number = input("Enter a 5 digit number: ")

    # Now loop through and count the sum
    sum = 0
    for ch in my_number:
        sum += int(ch)

    print("The total is:", sum)

main()