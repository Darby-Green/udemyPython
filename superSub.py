animals = {'turtle',
           'horse',
           'robin',
           'python',
           'swallow',
           'hedgehog',
           'wren',
           'aardvark',
           'cat',
           }
birds = {'robin', 'swallow', 'wren'}

print("*" * 40)
print(f'Birds is a subset of animals: {birds.issubset(animals)}')
print(f'Animals is a superset of birds: {animals.issuperset(birds)}')
print("*" * 40)