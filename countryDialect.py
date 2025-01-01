import csv

inputFilename = 'country_info.txt'

with open(inputFilename, encoding='utf-8', newline='') as countriesData:
    sample = ""
    for line in range(3):
        sample += countriesData.readline() #Goes to EOF
    countryDialect = csv.Sniffer().sniff(sample)
    # countriesData.seek(0) #Resets reader to beginning of the file
    countryReader = csv.reader(countriesData, dialect=countryDialect)
    for row in countryReader:
        print(row)

print("*" * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace'
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(countryDialect, attribute))}')