# Kilometre Convertor

def convert(num):
    return num * 0.6214


def main ():
    # Ask the user to enter a value for kms
    kms = float(input("Enter the number of KMs you wish to convert: "))
    miles = convert(kms)
    print ("That works out to", miles, "miles")

main()