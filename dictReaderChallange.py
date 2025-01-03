import csv

inputFileName = 'country_info.txt'
dialect = csv.excel
dialect.delimiter = '|'
countries = {}

with open(inputFileName, encoding='utf-8', newline='') as countryFile:
    headings = countryFile.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    dict_reader = csv.DictReader(countryFile, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = countryDict
        # countries[code.casefold()] = countryDict
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

#print(countries)

while True:
    chosenCountry = input('What country do you live in?: ')
    countryKey = chosenCountry.casefold()
    if countryKey in countries:
        countryData = countries[countryKey]
        print(f"The capital is {countryData['capital']}") #Can call dict keys from print
    elif chosenCountry == 'quit':
        break


