# Counts the number of times a T appears in a string

def main():
    # Create counter variable
    count = 0

    # Get the string
    my_string = input("Enter a sentence: ")

    # COunt the T's
    for ch in my_string:
        if ch == "t" or ch == "T":
            count += 1

    # Print results
    print("The letter T appears", count, "times")

main()