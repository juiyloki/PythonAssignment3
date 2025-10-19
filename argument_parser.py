import argparse

# Collects command arguments and returns a dictionary.

def parse_arguments():

    # Create the argumnent parser.

    parser = argparse.ArgumentParser()

    # Parse the arguments.

    # "-m", "--months": possible flags for user to call this argument.
    # nargs="+": for more than one value, nargs="*": optional.
    # required=True: self-explanatory.
    # default=[]: sets default value if user does not call it.
    # action="store_true"

    parser.add_argument(
        "-m", "--months", nargs="+", required=True,
        help="Lista miesięcy."
    )
    parser.add_argument(
        "-d", "--days", nargs="+", required=True,
        help="Zakresy dni tygodnia."
    )
    parser.add_argument(
        "-t", "--times", nargs="*", default=[],
        help="Pory dnia, domyślnie rano."
    )
    parser.add_argument(
        "-c", "--create", action="store_true",
        help="Tryb tworzenia plików. Jeśli nie podano, skrypt odczytuje dane."
    )

    # Read the command line input and store it in args.

    args = parser.parse_args()

    # Place the values from args into a dictionary for readability.

    args_dict = {
        "months": args.months,
        "days": args.days,
        "times": args.times,
        "create": args.create,
    }

    # return argument values as a dictionary.

    return args_dict


# Converts ranges of days to list of days.

def list_days(day_args: list[str]) -> list[list[str]]:

    WEEKDAYS = ["pn", "wt", "śr", "czw", "pt", "sb", "nd"]
    result = []

    # Iterate over each day range.

    for item in day_args:

        # item.strip().lower() to get rid of whitespaces.

        item = item.strip().lower()
        days_for_month = []

        # If the range is given (ex. pn-śr) extend it to the list.
        # Else just add the element.

        if '-' in item:

            # Get indexes in WEEKDAYS array from start and end of range.

            start, end = item.split('-')
            start_index = WEEKDAYS.index(start)
            end_index = WEEKDAYS.index(end)

            # Extend the ranges to get full lists.

            if start_index <= end_index:
                days_for_month.extend(WEEKDAYS[start_index:end_index + 1])
            else:  # wrap-around
                days_for_month.extend(WEEKDAYS[start_index:] + WEEKDAYS[:end_index + 1])

        else:
            days_for_month.append(item)

        # Add the list of the days this month to the overall list.

        result.append(days_for_month)

    return result