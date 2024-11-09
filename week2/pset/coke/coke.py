def main():
    change = insert_coin()
    print(f"Change Owed: {change}")



def insert_coin():
    amount = 50

    while True:
        print(f"Amount Due: {amount}")
        coin_inserted = int(input("Insert Coin: "))
        if coin_inserted in [25, 10, 5]:
            amount -= coin_inserted

        if amount <= 0:
            return amount * -1


main()
