from pathlib import Path
from make_read_csv import read_csv
from make_read_csv import make_csv


# Takes lists of preformatted strings containing directory names,
# creates paths to directories and generates a csv file in each one.
#
# example usage:
# `generate_csv_files(["Styczeń", "Luty"], [["wtorek", "środa"], ["piątek"]],
#                ["rano", "wieczorem"])`
def generate_csv_files(
    months: list[str],
    ranges_of_days: list[list[str]],
    times_of_days: list[str],
) -> None:
    for i in range(len(months)):
        for day in ranges_of_days[i]:
            time = times_of_days[i] if i < len(times_of_days) else "rano"
            path = Path.cwd() / months[i] / day / time

            path.parent.mkdir(parents=True, exist_ok=True)
            make_csv(path)

# Takes lists of preformatted strings containing directory names,
# constructs paths to files in specified directories, 
# returns the sum of times in the A column from each file.
#
# example usage:
# `A_time = read_csv_files(["Styczeń", "Luty"], [["wtorek", "środa"], ["piątek"]], 
#                          ["rano", "wieczorem"])`
def read_csv_files(
    months: list[str],
    ranges_of_days: list[list[str]],
    times_of_days: list[str],
) -> int:
    sum_of_times_in_A = 0
    for i in range(len(months)):
        for day in ranges_of_days[i]:
            time = times_of_days[i] if i < len(times_of_days) else "rano"
            path = Path.cwd() / months[i] / day / time

            sum_of_times_in_A += read_csv(path)

    return sum_of_times_in_A
