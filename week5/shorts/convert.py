def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU is {convert(au)} m")


def convert(au):
    if not isinstance(au, (int, float)) and au != 0:
        raise TypeError("au must be an integer or float")
    elif isinstance(au, int):
        au = float(au)
    return au * 149597870700


if __name__ == "__main__":
    main()
