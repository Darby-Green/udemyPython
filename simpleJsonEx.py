import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

#with open('test.json', 'w', encoding='utf-8') as testFile:
   # json.dump(languages, testFile)

with open('test.json', 'r', encoding='utf-8') as testFile:
    data = json.load(testFile)

print(data)
print(data[2])
