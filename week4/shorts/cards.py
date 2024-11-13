import random

cards = ["jack", "queen", "king"]


def main():
    # random.seed(1) -> This helps to debug a code by always providing the same random elements of a seed
    print(f"\n1 card: {random.choice(cards)}")

    # Replacement is like ["queen", "queen"] He can repeat the same item
    print(f"2 card with replacement: {random.choices(cards, k=2)}")

    # No replacement == cannot repeat the same item
    print(f"2 card without replacement: {random.sample(cards, k=2)}")

    # Jack has 75%, Queen has 10% and the king has 15% to be choiced
    print(f"1 card with weights: {random.choices(cards, weights=[75, 10, 15], k=1)} \n")


main()
