# Return value example

def main():
    # Get user's age
    first_age = int(input("Enter your age: "))

    # Get user's friends age
    second_age = int(input("Enter your friend's age: "))

    # get the sum of both ages
    total = sum(first_age, second_age)

    print ("Together you are", total, "years old")

# Sum function accepts to numbers and returns the sum
def sum(num1, num2):
    result = num1 + num2
    return result

main()