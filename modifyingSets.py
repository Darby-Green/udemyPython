numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     nextvalue = int(input("Please enter your next value: "))
#     numbers.add(nextvalue)
# print(numbers)

data = ['blue', 'red', 'blue', 'green', 'red', 'blue', 'white']

uniqueData = sorted(set(data))
print(uniqueData)

uniqueData = list(dict.fromkeys(data))
print(uniqueData)

print()
print(dict.fromkeys(data))