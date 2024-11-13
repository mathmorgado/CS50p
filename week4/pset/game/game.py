import random


def main():
    level = get_level("Level: ")
    secret_number = random.randint(1, level)
    get_guess("Guess: ", secret_number)


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
        except ValueError:
            continue

        if level > 0:
            return level

def get_guess(prompt, secret_number):
    while True:
        try:
            guess = int(input(prompt))
        except ValueError:
            continue

        if guess > secret_number:
            print("Too large!")
        elif guess < secret_number:
            print("Too small!")
        else:
            print("Just right!")
            return


if __name__ == "__main__":
    main()
