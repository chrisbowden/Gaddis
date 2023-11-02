# Function to accept a list
# anc calc the the sum

def main():
    numbers = [1,6,11,16,21]
    print(sum_list(numbers))


def sum_list(values_list):
    total = 0
    for item in values_list:
        total += item

    return total


main()