import csv

cerealFilename = 'cereal_grains.csv'

with open(cerealFilename, 'r', encoding='utf-8', newline='') as cerealFile:
    reader = csv.DictReader(cerealFile)
    for row in reader:
        print(row)