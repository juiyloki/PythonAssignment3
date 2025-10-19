from csv import DictReader
from pathlib import Path
import random

# Checks if file exists and returns it's time parameter if model = 'A'
def read_csv(path: Path):
    csv_file = path / 'Dane.csv'

    # Check if file exists in the given folder 
    if csv_file.exists():
        with open(csv_file, 'r') as csv_file:

            # Moves a file pointer to the second line
            reader = DictReader(csv_file, delimiter=';')
            row = next(reader)

            # Checks for 'A' model
            if row['Model'].strip() == 'A':
                return int(row[' Czas'].rstrip('s'))
    return 0

# Creates a new CSV file in the specified folder
def make_csv(path: Path):
    mlist = ['A', 'B', 'C']

    # Randomise file contents
    model = random.choice(mlist)
    score = random.randint(0, 1000)
    time = random.randint(0, 1000)

    # Create file name at the end of given path
    csv_file = path / 'Dane.csv'

    # Creates or overwrites file if it already exists
    csv_file.write_text(f'Model; Wynik; Czas;\n{model}; {score} ; {time}s;')

