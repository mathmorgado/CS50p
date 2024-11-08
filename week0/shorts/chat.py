# Global scope variable == Can be *accessed* throughout the code, but cannot be changed in local scopes
emoticon = "V.V"


def main():
    # Allow to changing a global variable
    global emoticon

    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
