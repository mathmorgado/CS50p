def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        number = int(input("Number: "))
        if number > 0:
            return number


def meow(n):
    for _ in range(n):
        print("meow")


main()
