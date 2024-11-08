def main():
    greet = input("Greeting: ").strip().lower()
    if not (greet[0] == "h"):
        print("$100")
        return

    if greet[:5] == "hello":
        print(f"$0")
    else:
        print(f"$20")


main()
