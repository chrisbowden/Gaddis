# Shows how to get and items location in a list
# and replace that item

def main():
    # Create the list
    food = ["Pizza", "Burgers", "Chips"]

    # Display the list
    print("Here are the items on the food list")
    print(food)

    # Get the item to change
    item = input("Which item should I change? ")

    try:
        # Get the item's index number
        item_index = food.index(item)

        # Get replacement value
        new_item = input("Enter the new value: ")

        # Replace the item
        food[item_index] = new_item

        # Display the new list
        print("Here is the revised list: ")
        print(food)
    except ValueError:
        print("That item was not found in the list")


main()
