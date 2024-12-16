import csv

fileName = 'cereal_grains.csv'

with open(fileName, encoding='utf-8', newline='') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)