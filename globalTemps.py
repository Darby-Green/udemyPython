import json
import urllib.request


jsonData = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

#with open(jsonData, encoding='utf-8') as data:
with urllib.request.urlopen(jsonData) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

#print(anomalies['citation']) no citation in file


