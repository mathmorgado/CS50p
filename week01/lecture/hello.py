def main():
    # Ask user fot their name
    username = input("What's your name? ").strip().title()
    hello(username)


def hello(to="world"):
    if to != "world" and " " in to:
        first_name, *last_name = to.split(" ")
        to = f"{first_name} {last_name[-1]}"

    print(f"Hello, {to}!")


main()
