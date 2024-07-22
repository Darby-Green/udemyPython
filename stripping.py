fileName = 'Jabberwocky.txt'

with open(fileName) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'"
noAp = first.strip(chars)
print(noAp)

