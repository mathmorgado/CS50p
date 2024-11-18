def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        # Split it using "/" as the separator
        fraction = fraction.split("/")

        try:
            # Converts each part to a int and assigns them to variables
            first_digit, second_digit = [int(digit) for digit in fraction]
            result = round((first_digit / second_digit) * 100)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

        # If the numerator is greater than the denominator, skip the current iteration
        if first_digit > second_digit:
            raise ValueError

        return result


def gauge(percentage):
    # Returns "E" for "Empty" when the results is less than or equal to 1%
    if percentage <= 1:
        return "E"
    # Returns "F" for "Full" when the results is 99% or more
    elif percentage >= 99:
        return "F"
    # Otherwise, returns the calculated percentage
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
