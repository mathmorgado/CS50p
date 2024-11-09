def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if plate length is between 2 and 6
    if 2 > len(plate) or len(plate) > 6:
        return False

    char_position = 1 # Position tracker for each character in plate
    is_first_digit = True # Flag to identify if it is the first digit
    for char in plate:
        # Check for invalid characters
        if char in [" ", ".", ",", "!", "#", "?"]:
            return False

        # Check for digits
        elif char.isdigit() and is_first_digit:
            if char == "0": # The first digit cannot be "0"
                return False
            elif char_position <= 2: # Digits cannot be in the first two positions
                return False
            is_first_digit = False

        # Check if all characters after a digit are also digits
        elif not is_first_digit and not char.isdigit():
            return False

        char_position += 1

    return True

main()
