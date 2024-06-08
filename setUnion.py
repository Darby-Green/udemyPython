# farmAnimals = {"sheep", "hen", "cow", "horse", "goat"}
# wildAnimals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# allAnimals = farmAnimals.union(wildAnimals)
# print(allAnimals)


from perscriptionData import adverse_interactions

medsToWatch= set()

# for interaction in adverse_interactions:
#     # medsToWatch = medsToWatch.union(interaction)
#     medsToWatch.update(interaction)

medsToWatch.update(*adverse_interactions)

print(sorted(medsToWatch))
print(*sorted(medsToWatch), sep='\n')