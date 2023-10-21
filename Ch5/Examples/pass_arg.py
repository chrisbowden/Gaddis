# This program demonstrates an argument being passed
# to a function

def main():
    value = 5
    show_double(value)


def show_double(number):
    result = number * 2
    print(result)

main()