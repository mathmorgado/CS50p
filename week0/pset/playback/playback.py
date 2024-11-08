def main():
    playback = get_phrase().replace(" ", "...")
    print(playback)


def get_phrase():
    phrase = input()
    return phrase


main()
