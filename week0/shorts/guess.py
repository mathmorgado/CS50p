def get_guess():
    guess = input("Guess: ").strip().lower()
    return guess # return value


def main():
    guess = get_guess()
    if guess in ["50", "fifty"]:
        print("Correct!") # side effect
    else:
        print("Wrong!") # side effect


main()
