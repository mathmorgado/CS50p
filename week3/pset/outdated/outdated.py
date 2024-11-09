months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_date("Date: ")
    print(date)


def get_date(prompt):
    while True:
        try:
            # Get date input and standardize it with title case
            date_input = input(prompt).title().strip()
        except EOFError:
            return ""

        # Split the date into parts based on format
        if "/" in date_input:
            date_parts = date_input.split("/")
            if any([not i.isdigit() for i in date_parts]):
                continue
        else:
            date_parts = date_input.split(" ")
            if "," not in date_parts[1]:
                continue

            date_parts[1] = date_parts[1].replace(",", "")

        # Validate the date and convert to the required format
        result = converted_date(date_parts)
        if result is not None:
            return result


def converted_date(date_parts):
    # If month is a number (MM/DD/YYYY format)
    if date_parts[0].isdigit():
        month, day, year = date_parts
    else:
        # If month is a name
        month_name, day, year = date_parts
        if month_name not in months: # Checking if the month is a valid month
            return None
        month = f"{months.index(month_name) + 1:02}"  # Convert month name to two-digit number


    # Check if day is a number and ensure month and day are within valid ranges
    if not (day.isdigit()) or not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            return None

    return f"{year}-{int(month):02}-{int(day):02}"


main()
