import inflect


def main():
    inf_lib = inflect.engine()
    names = inf_lib.join(get_names("Name: "))

    print("Adieu, adieu, to " + names)


def get_names(prompt):
    list_names = []
    while True:
        try:
            name = input(prompt)
        except EOFError:
            return list_names

        list_names.append(name)


if __name__ == "__main__":
    main()
