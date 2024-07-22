
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

#plantsFileName = 'flowersPrint.txt'

#with open(plantsFileName, 'w') as plants:
    #for plant in data:
        #print(plant, file=plants)


#newList = []
#with open(plantsFileName) as plants:
    #for plant in plants:
        #newList.append(plant.rstrip())

#print(newList)


plantsFilename = "flowersWrite.txt"

with open(plantsFilename,'w') as plants:
    for plant in data:
        plants.write(plant)










