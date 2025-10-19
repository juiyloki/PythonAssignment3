from csv import DictReader
from pathlib import Path
import random

#checks if file and returns time if model = 'A'
def read_csv(path: Path):
    csv_file = path / 'Dane.csv'

    if csv_file.exists():
        with open(csv_file, 'r') as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            row = next(reader)

            if row['Model'].strip() == 'A':
                return int(row[' Czas'].rstrip('s'))
    return 0

def make_csv(path: Path):
    mlist = ['A', 'B', 'C']

    model = random.choice(mlist)
    score = random.randint(0, 1000)
    time = random.randint(0, 1000)
    csv_file = path / 'Dane.csv'

    csv_file.write_text(f'Model; Wynik; Czas;\n{model}; {score} ; {time}s;')

