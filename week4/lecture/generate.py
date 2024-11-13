import random as r

cards = ["King", "Queen", "Jack"]

coin = r.choice(["heads", "tails"])
rand_int = r.randint(1, 10)
r.shuffle(cards)

print(f"\nCoin: {coin}")
print(f"Random integer: {rand_int}")
print(f"Sequence of cards: {cards}\n")
