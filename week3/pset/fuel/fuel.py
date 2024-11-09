def main():
    fraction = get_fraction("Fraction: ")
    print(fraction)


def get_fraction(prompt):
    while True:
        # Gets input and splits it using "/" as the separator
        fraction = input(prompt)
        fraction = fraction.split("/")

        try:
            # Converts each part to a float and assigns them to variables
            first_digit, second_digit = [int(digit) for digit in fraction]
            result = (first_digit / second_digit) * 100
        except (ValueError, ZeroDivisionError):
            continue

        # If the numerator is greater than the denominator, skip the current iteration
        if first_digit > second_digit:
            continue
        # Ensures both numbers are integers, if not, skips the current iteration
        elif not isinstance(first_digit, int) or not isinstance(second_digit, int):
            continue

        # Returns "E" for "Empty" when the results is less than or equal to 1%
        if result <= 1:
            return "E"
        # Returns "F" for "Full" when the results is 99% or more
        elif result >= 99:
            return "F"
        # Otherwise, returns the calculated percentage
        else:
            return f"{result:.0f}%"


main()
