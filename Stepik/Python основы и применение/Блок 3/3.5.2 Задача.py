import csv
import re

pattern = r'\d{2}/\d{2}/(\d{4})'
crimes = dict()

counter = 0
name = str()
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            if re.match(pattern, row[2]).group(1) == '2015':
                if row[5].upper() not in crimes:
                    crimes[row[5].upper()] = 1
                else:
                    crimes[row[5].upper()] += 1
        except:
            continue
for key, value in crimes.items():
    if value > counter:
        counter = value
        name = key

print(name, counter)
