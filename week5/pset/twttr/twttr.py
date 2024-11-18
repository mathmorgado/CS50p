def main():
    tweet = input("Input: ")
    twttr = shorten(tweet)

    print(f"Output: {twttr}")


def shorten(word):
    twttr = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            twttr += letter

    return twttr


if __name__ == "__main__":
    main()
