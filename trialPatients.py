# trial1 = {"Bob", "Charley", "Georgia", "John"}
# trial2 = {"Anne", "Charley", "Eddie", "Georgia"}
#
# checkSet  = trial1.intersection(trial2)
# print(checkSet)


farmAnimals = {"sheep", "hen", "cow", "horse", "goat"}
wildAnimals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potentialRides = {"donkey", "horse", "camel"}

intersection = farmAnimals & wildAnimals & potentialRides
print(intersection)

mounts = farmAnimals.intersection(wildAnimals, potentialRides)
print(mounts)