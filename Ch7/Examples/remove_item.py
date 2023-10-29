# Remove from a list

def main():
    # Create the list
    food = ["Pizza", "Burgers", "Chips"]

    # Display the list
    print("Here are the items on the food list")
    print(food)

    # Get the item to change
    item = input("Which item should I remove? ")

    try:
        # Remove the item
        food.remove(item)

        # Display the list
        print("Here is the revised list:")
        print(food)

    except ValueError:
        print("That item was not found in the list.")

main()
