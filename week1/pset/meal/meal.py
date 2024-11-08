def main():
    time = input("What's time is it? ").strip().lower()
    time_converted = convert(time)

    if 7 <= time_converted < 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")


def convert(time):
    time_parts = time.split(":")
    hour = float(time_parts[0])
    minutes_and_period = time_parts[1].split()

    minutes = float(minutes_and_period[0])

    if len(minutes_and_period) > 1:
        period = minutes_and_period[1]
        if period in ["p.m", "pm"] and hour != 12:
            hour += 12

    return hour + minutes / 60.0


if __name__ == "__main__":
    main()
