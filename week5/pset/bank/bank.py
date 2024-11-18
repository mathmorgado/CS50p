def main():
    greet = input("Greeting: ")
    print(greeting(greet))


def greeting(greet):
    if not isinstance(greet, str):
        raise TypeError("Greet must be a string")
    greet = greet.strip().lower()
    if not (greet[0] == "h"):
        return "$100"

    if greet[:5] == "hello":
        return "$0"
    else:
        return "$20"


if __name__ == "__main__":
    main()
