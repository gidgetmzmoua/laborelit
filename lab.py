import csv

with open('sample.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['a'])  # Accessing a specific value using dictionary keys
