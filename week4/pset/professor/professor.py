"""
In this code, we need to:
    - Get the level [1, 2, 3]
    - Randomly generate 10 math problems (X + Y = ). Obs: X and Y are a non-negative integer
    - If the answer is not correct, output "EEE". If the user wrong 3 times, output the correct answer (X + Y = Z)
    - Output the score (-1 for each problem missed 3 times)
"""

import random

NUM_PROBLEMS = 10
TRIES = 3


def main():
    level = get_level("Level: ")
    score = 0

    for _ in range(NUM_PROBLEMS):
        score += generate_math_problem(level, TRIES)

    print(f"Score: {score}")


def get_level(prompt):
    """ Prompt for a level between 1 and 3 """
    while True:
        level = get_non_negative_integer(prompt)
        return level


def generate_math_problem(level, tries=3):
    """Generate and evaluete a math problem, returning a score"""
    x, y = generate_integers(level)
    for _ in range(tries):
        answer = get_non_negative_integer(f"{x} + {y} = ")
        if answer == (x + y):
             return 1
        else:
            print("EEE")

    print(f"{x} + {y} = {x + y}")
    return 0


def generate_integers(level):
    """Generete two random integers based on the level of difficulty"""
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)


def get_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            continue


if __name__ == "__main__":
    main()
