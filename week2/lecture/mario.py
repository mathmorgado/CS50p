def main():
    height = get_height()
    pyramid(height)


def get_height():
    while True:
        height = int(input("Height: "))
        if 0 < height < 9:
            return height
        else:
            print("Please, take a number between 1 and 8!\n")


def pyramid(h):
    for row in range(1, h+1):
        print(" " * (h-row), "#" * row, sep="", end=" ")
        print("#" * row)


main()
