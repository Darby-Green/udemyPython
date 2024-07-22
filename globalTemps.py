import json

jsonData = 'data.json'

with open(jsonData, encoding='utf-8') as data:
    anomalies = json.load(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

#print(anomalies['citation']) no citation in file


