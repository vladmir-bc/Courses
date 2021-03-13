import csv

with open('example2.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    print(reader)
    for row in reader:
        print(row)
