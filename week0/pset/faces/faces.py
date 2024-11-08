happy_emoticon = "🙂"
sad_emoticon = "🙁"

def main():
    phrase_emoticon = get_phrase().replace(":)", happy_emoticon).replace(":(", sad_emoticon)

    print(phrase_emoticon)


def get_phrase():
    phrase = input()
    return phrase


main()
