import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
          ]

keys = ['album', 'artist', 'year']

fileName = 'albums.csv'
with open(fileName, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        zipObject = zip(keys, row)
        # print(zipObject)
        # for thing in zip(keys, row):
        #     print("\t", thing)
        albumDict = dict(zipObject)
        print(albumDict)
        writer.writerow(albumDict)

