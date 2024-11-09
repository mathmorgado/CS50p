distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    else:
        print(f"{convert_au_to_m(au)}m")

def convert_au_to_m(au):
    return au * 149597870700


main()
