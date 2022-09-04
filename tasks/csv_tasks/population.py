"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
from pathlib import Path
import csv


def max_delta(population):
    year_percent = 0
    with open(population, "r") as f_p:
        reader = csv.reader(f_p)
        count = 0
        year = 0
        for row in reader:
            if count == 0:
                pass
            else:
                n = float(row[2])
                if n > year_percent:
                    year_percent = n
                    year = int(row[0])
            count += 1
    print(str(year))


max_delta(Path("world_population.csv"))
