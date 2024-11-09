def main():
    # Calls the function to get the grocery list, then prints each item
    grocery_list = get_grocery_list()
    for item in grocery_list:
        print(item)


def get_grocery_list():
    grocery_list = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            # Returns a sorted list of items in the format "quantity ITEM"
            return [f"{qty} {item}" for item, qty in sorted(grocery_list.items())]

        # If the item is not already in the list, adds it with a quantity of 1
        if item not in grocery_list.keys():
            grocery_list[item] = 1
        # If the item is already in the list, increments its quatity by 1
        else:
            grocery_list[item] += 1


main()
