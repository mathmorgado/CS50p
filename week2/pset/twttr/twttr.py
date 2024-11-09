def main():
    tweet = input("Input: ")
    twttr = convert_to_twttr(tweet)

    print(f"Output: {twttr}")

def convert_to_twttr(tweet):
    twttr = ""
    for letter in tweet:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            twttr += letter

    return twttr


main()
