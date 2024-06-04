farmAnimals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

print()
print("Indexing a sequence")
animalsList = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animalsList[3]
print(goat)

moreAnimals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if moreAnimals == farmAnimals:
    print("These sets are equal")
else:
    print("These sets are not equal")