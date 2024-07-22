
inputFileName = 'country_info.txt'

countries = {}

with open(inputFileName, 'r') as countryFile:
    countryFile.readline()
    for row in countryFile:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        #print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        
        countryDict = {
                'name': country,
                'capital': capital,
                'countryCode': code,
                'cc3': code3,
                'dialingCode': dialing,
                'timezone': timezone,
                'currency': currency,
                }
        #print(countryDict)
        countries[country.casefold()] = countryDict
        countries[code.casefold()] = countryDict

#print(countries)

while True:
    question = input('What country do you live in?: ').casefold()
    if question in countries:
        answermk1 = countries[question]
        print(f"The capital is {answermk1['capital']}") #Can call dict keys from print
    elif question == 'quit':
        break


