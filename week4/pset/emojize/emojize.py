from emoji import emojize


def main():
    prompt = input("Input: ")
    emoji = emojize(prompt, language="alias")
    print(emoji)


main()
