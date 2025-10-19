from pathlib import Path
from make_read_csv import read_csv
from make_read_csv import make_csv


def format_day(day: str) -> str:
    formatted_days = {
        "pn": "poniedziałek",
        "wt": "wtorek",
        "śr": "środa",
        "czw": "czwartek",
        "pt": "piątek",
        "sb": "sobota",
        "nd": "niedziela",
    }
    return formatted_days[day]


def format_time(time: str) -> str:
    formatted_times = {"r": "rano", "w": "wieczorem"}
    return formatted_times[time]


def create_path(month: str, day: str, time: str) -> Path:
    path = Path.cwd() / month.capitalize() / format_day(day) / format_time(time)
    return path


# Takes lists of preformatted strings containing directory names,
# creates paths to directories and generates a csv file in each one.
#
# example usage:
# `generate_csv_files(["styczeń", "luty"], [["wt", "śr"], ["pt"]],
#                ["r", "w"])`
def generate_csv_files(
    months: list[str],
    ranges_of_days: list[list[str]],
    times_of_days: list[str],
) -> None:
    time_index = 0

    for i in range(len(months)):
        for day in ranges_of_days[i]:
            time = (
                times_of_days[time_index] if time_index < len(times_of_days) else "r"
            )
            time_index += 1

            path = create_path(months[i], day, time)

            path.mkdir(parents=True, exist_ok=True)
            make_csv(path)


# Takes lists of preformatted strings containing directory names,
# constructs paths to files in specified directories,
# returns the sum of times in the A column from each file.
#
# example usage:
# `A_time = read_csv_files(["styczeń", "luty"], [["wt", "śr"], ["pt"]],
#                          ["r", "w"])`
def read_csv_files(
    months: list[str],
    ranges_of_days: list[list[str]],
    times_of_days: list[str],
) -> None:
    sum_of_times_in_A = 0
    time_index = 0

    for i in range(len(months)):
        for day in ranges_of_days[i]:
            time = (
                times_of_days[time_index] if time_index < len(times_of_days) else "r"
            )
            time_index += 1

            path = create_path(months[i], day, time)

            sum_of_times_in_A += read_csv(path)

    print("Suma czasów Modelu A wynosi ", sum_of_times_in_A, "s", sep="")
