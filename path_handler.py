import os
from pathlib import Path
from typing import Callable
from make_read_csv import read_csv
from make_read_csv import make_csv


# Takes lists of preformatted strings containing directory names,
# creates paths to directories and performs `action` on each path.
# `action` can be either `generate_file` or `read_file`
#
# example usage:
# `process_paths(["Styczeń", "Luty"], [["wtorek", "środa"], ["piątek]],
#                ["rano", "wieczorem"], read_file)`
def process_paths(
    months: list[str],
    ranges_of_days: list[list[str]],
    times_of_days: list[str],
    action: Callable[[Path], None],
):
    for i in range(len(months)):
        for day in ranges_of_days[i]:
            time = times_of_days[i] if i < len(times_of_days) else "rano"
            path = Path.cwd() / months[i] / day / time
            action(path)


def generate_file(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    make_csv(path)


def read_file(path: Path):
    read_csv(path)
