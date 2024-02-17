yeet = input("Please enter some numbers: ")
seperators = ""
for char in yeet:
    if not char.isnumeric():
        seperators = seperators + char


print(seperators)

values = "".join(char if char not in seperators else " " for char in yeet).split()
print(sum([int(val)for val in values]))