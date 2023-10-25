

def feet_to_inches(number):
    return number * 12

def main():
    feet = int(input("Enter the number of feet: "))
    inches = feet_to_inches(feet)
    print("The number of inches is:", inches)

main()