import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if not validate_args(sys.argv, available_fonts):
        sys.exit("Invalid usage")

    # Set the font if specified
    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])

    text = input("Input: ")
    print(f"Output: \n{figlet.renderText(text)}")


def validate_args(args, available_fonts):
    # Check if it has 1 or 3 arguments
    if len(args) not in [1, 3] :
        return False
    # if has 3 argv, check if there is -f/--font in the commands
    elif len(args) == 3:
        # Check if the font is available and if -f/--font is in the commands
        return args[2] in available_fonts if args[1] in ["-f", "--font"] else False

    return True


main()
