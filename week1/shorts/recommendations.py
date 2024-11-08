def main():
    difficulty = input("Difficult or Casual? ").strip().lower()
    if not (difficulty in ["difficult", "casual"]):
        print("Enter a valid difficulty!")
        return

    players = input("Multiplayer or Single-player? ").strip().lower()
    if not (players in ["multiplayer", "single-player", "singleplayer"]):
        print("Enter a valid number of players!")
        return

    if difficulty == "difficult" and players == "multiplayer":
        recommend("Poker")
    elif difficulty == "difficult" and players in ["single-player", "singleplayer"]:
        recommend("Klondike")
    elif difficulty == "casual" and players == "multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game):
    print(f"You might like {game}!")


main()
