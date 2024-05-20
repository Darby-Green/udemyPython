animals = {
    "lion": ["scary"],
    "elephant": ["big"],
    "teddy": ["cuddly"]
}

# def deepCopy(d):
#     newdict = {}
#     for key, value in d.items():
#         newdict[key] = value
#     return newdict

def deepCopy2(d: dict):
    newDict = {}
    for key, value in d.items():
        newValue = value.copy()
        newDict[key] = newValue
    return newDict

animalsCopy = deepCopy2(animals)
animalsCopy["teddy"].append("fluffy")

print(animalsCopy)
print(animals)



