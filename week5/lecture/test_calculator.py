from calculator import square


def main():
    tests = [[2, 4], [3, 9], [0, 0], [-2, 4], [-3, 9]]
    for test in tests:
        try:
            assert square(test[0]) == test[1]
        except AssertionError:
            print(f"{test[0]} squared was not {test[1]}!")


if __name__ == "__main__":
    main()
