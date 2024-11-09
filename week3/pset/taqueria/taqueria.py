items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = get_items("Item: ", items)
    print(total)


def get_items(prompt, items):
    accumulator = 0
    while True:
        try:
            item = input(prompt).title()
            accumulator += items[item]
        except (EOFError, KeyboardInterrupt):
            return ''
        except KeyError:
            continue

        print(f"Total: ${accumulator:.2f}")


main()
