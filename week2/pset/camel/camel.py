def main():
    camelCase = input("camelCase: ")
    print(f"snake_case: {convert_to_snake_case(camelCase)}")


def convert_to_snake_case(camelCase):
    snake_case = ""
    for letter in camelCase:
        if letter.isupper() :
            snake_case += "_"
        snake_case += letter.lower()
    return snake_case


main()
