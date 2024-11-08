def main():
    expression = input("Expression: ").strip().split(" ")
    calculate(expression)


def calculate(expression):
    first_number = float(expression[0])
    second_number = float(expression[2])
    operator = expression[1]

    match operator:
        case '+':
            print(first_number + second_number)
        case '-':
            print(first_number - second_number)
        case '*':
            print(first_number * second_number)
        case '/':
            print(first_number / second_number)


main()
