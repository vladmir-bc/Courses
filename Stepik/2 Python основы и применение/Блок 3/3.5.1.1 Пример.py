import csv

with open('example3.csv') as f:
    reader = csv.reader(f)
    print(reader)  # <_csv.reader object at 0x014B2D70>
    for row in reader:
        print(row)