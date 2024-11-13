import sys
import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        number_of_bitcoin = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Request Error")

    bitcoin_quote = response["bpi"]["USD"]["rate_float"]
    amount = bitcoin_quote * number_of_bitcoin

    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
