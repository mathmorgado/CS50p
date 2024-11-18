def main():
    name = input("Name: ")
    print(hello(name))


def hello(to="World"):
    return f"Hello {to.strip().title()}!"


if __name__ == "__main__":
    main()
